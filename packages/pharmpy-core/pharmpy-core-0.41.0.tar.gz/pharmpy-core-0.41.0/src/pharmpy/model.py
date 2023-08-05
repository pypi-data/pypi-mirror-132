"""
===================
Generic Model class
===================

**Base class of all implementations.**

Inherit to *implement*, i.e. to define support for a specific model type. Duck typing is utilized,
but an implementation is expected to implement **all** methods/attributes.

Definitions
-----------
"""

import copy
import re
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.linalg
import sympy

import pharmpy.symbols
from pharmpy import Parameters, RandomVariables
from pharmpy.workflows import default_model_database


def canonicalize_data_transformation(model, value):
    if value is None:
        value = model.dependent_variable
    else:
        value = sympy.sympify(value)
        if value.free_symbols != {model.dependent_variable}:
            raise ValueError(
                f"Expression for data transformation must contain the dependent variable "
                f"{model.dependent_variable} and no other variables"
            )
    return value


class ModelException(Exception):
    pass


class ModelSyntaxError(ModelException):
    def __init__(self, msg='model syntax error'):
        super().__init__(msg)


class Model:
    """
    Attribute: name
       dependent_variable
       parameters
       random_variables
       statements
       dataset
    """

    def __init__(self):
        self.modelfit_results = None

    def to_generic_model(self):
        """Convert a model into the base model class"""
        model = Model()
        model.parameters = self.parameters.copy()
        model.random_variables = self.random_variables.copy()
        model.statements = self.statements.copy()
        model.dataset = self.dataset.copy()
        model.name = self.name
        model.dependent_variable = self.dependent_variable
        model.estimation_steps = self.estimation_steps
        try:
            model.database = self.database
        except AttributeError:
            pass
        return model

    def __repr__(self):
        return f'<Pharmpy model object {self.name}>'

    def _repr_html_(self):
        stat = self.statements._repr_html_()
        rvs = self.random_variables._repr_latex_()
        return f'<hr>{stat}<hr>${rvs}$<hr>{self.parameters._repr_html_()}<hr>'

    @property
    def modelfit_results(self):
        return self._modelfit_results

    @modelfit_results.setter
    def modelfit_results(self, value):
        self._modelfit_results = value

    @property
    def data_transformation(self):
        """Transformation used for DV in dataset"""
        try:
            return self._data_transformation
        except AttributeError:
            return self.dependent_variable

    @data_transformation.setter
    def data_transformation(self, value):
        value = canonicalize_data_transformation(self, value)
        self._data_transformation = value

    def write(self, path='', force=False):
        """Write model to file using its source format
        If no path is supplied or does not contain a filename a name is created
        from the name property of the model
        Will not overwrite in case force is True.
        return path written to
        """
        path = Path(path)
        if not path or path.is_dir():
            try:
                filename = f'{self.name}{self.filename_extension}'
            except AttributeError:
                raise ValueError(
                    'Cannot name model file as no path argument was supplied and the'
                    'model has no name.'
                )
            path = path / filename
            new_name = None
        else:
            # Set new name given filename, but after we've checked for existence
            new_name = path.stem
        if not force and path.exists():
            raise FileExistsError(f'File {path} already exists.')
        if new_name:
            self.name = new_name
        self.update_source(path=path, force=force)
        if not force and path.exists():
            raise FileExistsError(f'Cannot overwrite model at {path} with "force" not set')
        with open(path, 'w', encoding='latin-1') as fp:
            fp.write(self.model_code)
        self.database = default_model_database(path=path.parent)
        return path

    def update_inits(self):
        """Update inital estimates of model from its own ModelfitResults"""
        if self.modelfit_results:
            self.parameters = self.modelfit_results.parameter_estimates
        else:
            # FIXME: Other exception here. ModelfitError?
            raise ModelException(
                "Cannot update initial parameter estimates " "since parameters were not estimated"
            )

    def copy(self):
        """Create a deepcopy of the model object"""
        return copy.deepcopy(self)

    def update_individual_estimates(self, source):
        self.initial_individual_estimates = source.modelfit_results.individual_estimates

    def read_raw_dataset(self, parse_columns=tuple()):
        raise NotImplementedError()

    def bump_model_number(self, path='.'):
        """If the model name ends in a number increase it to next available file
        else do nothing.
        """
        path = Path(path)
        name = self.name
        m = re.search(r'(.*?)(\d+)$', name)
        if m:
            stem = m.group(1)
            n = int(m.group(2))
            while True:
                n += 1
                new_name = f'{stem}{n}'
                new_path = (path / new_name).with_suffix(self.filename_extension)
                if not new_path.exists():
                    break
            self.name = new_name

    def create_symbol(self, stem, force_numbering=False):
        """Create a new unique variable symbol

        Parameters
        ----------
        stem : str
            First part of the new variable name
        force_numbering : bool
            Forces addition of number to name even if variable does not exist, e.g.
            COVEFF --> COVEFF1
        """
        symbols = [str(symbol) for symbol in self.statements.free_symbols]
        params = [param.name for param in self.parameters]
        rvs = [rv.name for rv in self.random_variables]
        dataset_col = list(self.dataset.columns)
        misc = [self.dependent_variable]

        all_names = symbols + params + rvs + dataset_col + misc

        if str(stem) not in all_names and not force_numbering:
            return pharmpy.symbols.symbol(str(stem))

        i = 1
        while True:
            candidate = f'{stem}{i}'
            if candidate not in all_names:
                return pharmpy.symbols.symbol(candidate)
            i += 1

    def remove_unused_parameters_and_rvs(self):
        """Remove any parameters and rvs that are not used in the model statements"""
        symbols = self.statements.free_symbols

        new_rvs = RandomVariables()
        for rv in self.random_variables:
            # FIXME: change if rvs are random symbols in expressions
            if rv.symbol in symbols or not symbols.isdisjoint(rv.sympy_rv.pspace.free_symbols):
                new_rvs.append(rv)
        self.random_variables = new_rvs

        new_params = Parameters()
        for p in self.parameters:
            symb = p.symbol
            if symb in symbols or symb in new_rvs.free_symbols or (p.fix and p.init == 0):
                new_params.append(p)
        self.parameters = new_params

    def _observation(self):
        stats = self.statements
        for i, s in enumerate(stats):
            if s.symbol.name == 'Y':
                y = s.expression
                break

        for j in range(i, -1, -1):
            y = y.subs({stats[j].symbol: stats[j].expression})

        return y

    def symbolic_population_prediction(self):
        """Symbolic model population prediction"""
        y = self.symbolic_individual_prediction()
        for eta in self.random_variables.etas:
            y = y.subs({eta.name: 0})
        return y

    def symbolic_individual_prediction(self):
        """Symbolic model individual prediction"""
        y = self._observation()

        for eps in self.random_variables.epsilons:
            # FIXME: The rv symbol and the code symbol are different.
            y = y.subs({eps.name: 0})

        return y

    def population_prediction(self, parameters=None, dataset=None):
        """Numeric population prediction

        The prediction is evaluated at the current model parameter values
        or optionally at the given parameter values.
        The evaluation is done for each data record in the model dataset
        or optionally using the dataset argument.

        Return population prediction series
        """
        y = self.symbolic_population_prediction()
        if parameters is not None:
            y = y.subs(parameters)
        else:
            if self.modelfit_results is not None:
                y = y.subs(self.modelfit_results.parameter_estimates.to_dict())
            else:
                y = y.subs(self.parameters.inits)

        if dataset is not None:
            df = dataset
        else:
            df = self.dataset

        pred = df.apply(lambda row: np.float64(y.subs(row.to_dict())), axis=1)

        return pred

    def individual_prediction(self, etas=None, parameters=None, dataset=None):
        """Numeric individual prediction"""
        y = self.symbolic_individual_prediction()
        if parameters is not None:
            y = y.subs(parameters)
        else:
            y = y.subs(self.parameters.inits)

        if dataset is not None:
            df = dataset
        else:
            df = self.dataset

        idcol = self.datainfo.id_label

        if etas is None:
            if self.initial_individual_estimates is not None:
                etas = self.initial_individual_estimates
            else:
                etas = pd.DataFrame(
                    0,
                    index=df.pharmpy.ids,
                    columns=[eta.name for eta in self.random_variables.etas],
                )

        def fn(row):
            row = row.to_dict()
            curetas = etas.loc[row[idcol]].to_dict()
            a = np.float64(y.subs(row).subs(curetas))
            return a

        ipred = df.apply(fn, axis=1)
        return ipred

    def symbolic_eta_gradient(self):
        y = self._observation()
        for eps in self.random_variables.epsilons:
            y = y.subs({eps.name: 0})
        d = [y.diff(pharmpy.symbols.symbol(x.name)) for x in self.random_variables.etas]
        return d

    def symbolic_eps_gradient(self):
        y = self._observation()
        d = [y.diff(pharmpy.symbols.symbol(x.name)) for x in self.random_variables.epsilons]
        return d

    def _replace_parameters(self, y, parameters):
        if parameters is not None:
            y = [x.subs(parameters) for x in y]
        else:
            y = [x.subs(self.parameters.inits) for x in y]
        return y

    def eta_gradient(self, etas=None, parameters=None, dataset=None):
        """Numeric eta gradient

        The gradient is evaluated given initial etas, parameters and the model dataset.
        The arguments etas, parameters and dataset can optionally override those
        of the model. Return a DataFrame of gradients.
        """
        y = self.symbolic_eta_gradient()
        y = self._replace_parameters(y, parameters)

        if dataset is not None:
            df = dataset
        else:
            df = self.dataset
        idcol = self.datainfo.id_label

        if etas is None:
            if self.initial_individual_estimates is not None:
                etas = self.initial_individual_estimates
            else:
                etas = pd.DataFrame(
                    0,
                    index=df.pharmpy.ids,
                    columns=[eta.name for eta in self.random_variables.etas],
                )

        def fn(row):
            row = row.to_dict()
            curetas = etas.loc[row[idcol]].to_dict()
            a = [np.float64(x.subs(row).subs(curetas)) for x in y]
            return a

        derivative_names = [f'dF/d{eta.name}' for eta in self.random_variables.etas]
        grad = df.apply(fn, axis=1, result_type='expand')
        grad = pd.DataFrame(grad)
        grad.columns = derivative_names
        return grad

    def eps_gradient(self, etas=None, parameters=None, dataset=None):
        """Numeric epsilon gradient"""
        y = self.symbolic_eps_gradient()
        y = self._replace_parameters(y, parameters)
        eps_names = [eps.name for eps in self.random_variables.epsilons]
        repl = {pharmpy.symbols.symbol(eps): 0 for eps in eps_names}
        y = [x.subs(repl) for x in y]

        if dataset is not None:
            df = dataset
        else:
            df = self.dataset

        idcol = self.datainfo.id_label

        if etas is None:
            if self.initial_individual_estimates is not None:
                etas = self.initial_individual_estimates
            else:
                etas = pd.DataFrame(
                    0,
                    index=df.pharmpy.ids,
                    columns=[eta.name for eta in self.random_variables.etas],
                )

        def fn(row):
            row = row.to_dict()
            curetas = etas.loc[row[idcol]].to_dict()
            a = [np.float64(x.subs(row).subs(curetas)) for x in y]
            return a

        grad = df.apply(fn, axis=1, result_type='expand')
        derivative_names = [f'dY/d{eps}' for eps in eps_names]
        grad = pd.DataFrame(grad)
        grad.columns = derivative_names
        return grad

    def weighted_residuals(self, parameters=None, dataset=None):
        omega = self.random_variables.etas.covariance_matrix
        sigma = self.random_variables.epsilons.covariance_matrix
        if parameters is None:
            if self.modelfit_results is not None:
                parameters = self.modelfit_results.parameter_estimates.to_dict()
            else:
                parameters = self.parameters.inits
        omega = omega.subs(parameters)
        sigma = sigma.subs(parameters)
        omega = np.float64(omega)
        sigma = np.float64(sigma)
        if dataset is not None:
            df = dataset
        else:
            df = self.dataset
        # FIXME: Could have option to gradients to set all etas 0
        etas = pd.DataFrame(
            0, index=df.pharmpy.ids, columns=[eta.name for eta in self.random_variables.etas]
        )
        G = self.eta_gradient(etas=etas, parameters=parameters, dataset=dataset)
        H = self.eps_gradient(etas=etas, parameters=parameters, dataset=dataset)
        F = self.population_prediction()
        index = df[self.datainfo.id_label]
        G.index = index
        H.index = index
        F.index = index
        WRES = np.float64([])
        for i in df.pharmpy.ids:
            Gi = np.float64(G.loc[[i]])
            Hi = np.float64(H.loc[[i]])
            Fi = F.loc[i:i]
            DVi = np.float64(df['DV'][df[self.datainfo.id_label] == i])
            Ci = Gi @ omega @ Gi.T + np.diag(np.diag(Hi @ sigma @ Hi.T))
            WRESi = scipy.linalg.sqrtm(scipy.linalg.inv(Ci)) @ (DVi - Fi)
            WRES = np.concatenate((WRES, WRESi))
        return pd.Series(WRES)
