"""Contains the generic Prediction. This class represents any kind of prediction
interpreted as fitted array Y' attempting to be close to real array Y.

The Prediction class allows to compute some metrics concerning the accuracy
without needing to know how the prediction was computed.

The subclasses allow for metrics that are relevant for just specific types
of predictions."""

from typing import Union

import numpy as np
import pandas as pd

from easypred.type_aliases import VectorPdNp


class Prediction:
    """Class to represent a generic prediction.

    Attributes
    ----------
    real_values : Union[np.ndarray, pd.Series, list]
        The array-like object containing the N real values.
    fitted_values : Union[np.ndarray, pd.Series, list]
        The array-like object of length N containing the fitted values.
    """

    def __init__(
        self,
        real_values: Union[np.ndarray, pd.Series, list],
        fitted_values: Union[np.ndarray, pd.Series, list],
    ):
        """Class to represent a generic prediction.

        Arguments
        -------
        real_values: Union[np.ndarray, pd.Series, list]
            The array-like object containing the real values. It must have the same
            length of fitted_values. If list, it will be turned into np.array.
        fitted_values: Union[np.ndarray, pd.Series, list]
            The array-like object of length N containing the fitted values. If list,
            it will be turned into np.array.
        """
        self.real_values = real_values
        self.fitted_values = fitted_values

        # Processing appening at __init__
        self._check_lengths_match()
        self._lists_to_nparray()

    def _lists_to_nparray(self) -> None:
        """Turn lists into numpy arrays."""
        if isinstance(self.fitted_values, list):
            self.fitted_values = np.array(self.fitted_values)
        if isinstance(self.real_values, list):
            self.real_values = np.array(self.real_values)

    def _check_lengths_match(self) -> None:
        """Check that fitted values and real values have the same length."""
        len_fit, len_real = len(self.fitted_values), len(self.real_values)
        if len_fit != len_real:
            raise ValueError(
                "Fitted values and real values must have the same length.\n"
                + f"Fitted values has length: {len_fit}.\n"
                + f"Real values has length: {len_real}."
            )

    def __str__(self):
        return self.fitted_values.__str__()

    def __len__(self):
        return len(self.fitted_values)

    def __eq__(self, other):
        return np.all(self.fitted_values == other.fitted_values)

    def __ne__(self, other):
        return np.any(self.fitted_values != other.fitted_values)

    @property
    def accuracy_score(self) -> float:
        """Return a float representing the percent of items which are equal
        between the real and the fitted values."""
        return np.mean(self.real_values == self.fitted_values)

    def matches(self) -> VectorPdNp:
        """Return a boolean array of length N with True where fitted value is
        equal to real value."""
        return self.real_values == self.fitted_values

    def as_dataframe(self) -> pd.DataFrame:
        """Return prediction as a dataframe containing various information over
        the prediction quality."""
        data = {
            "Real Values": self.real_values,
            "Fitted Values": self.fitted_values,
            "Prediction Matches": self.matches(),
        }
        return pd.DataFrame(data)

    def describe(self) -> pd.DataFrame:
        """Return a dataframe containing some key information about the
        prediction."""
        return self._describe()

    def _describe(self) -> pd.DataFrame:
        """Return some basic metrics for the prediction."""
        n = len(self)
        matches = self.matches().sum()
        errors = n - matches
        return pd.DataFrame(
            {
                "N": [n],
                "Matches": [matches],
                "Errors": [errors],
                "Accuracy": [self.accuracy_score],
            },
            index=["Value"],
        ).transpose()
