"""Subclass of Prediction specialized in representing a binary prediction, thus
a prediction where both the fitted and real data attain at most two different
values.

It allows to compute accuracy metrics like true positive, true negative, etc."""
from __future__ import annotations

from typing import Any, Union

import numpy as np
import pandas as pd

from easypred import Prediction


class BinaryPrediction(Prediction):
    """Class to represent a binary prediction.

    Attributes
    -------
    fitted_values: Union[np.ndarray, pd.Series, list]
        The array-like object of length N containing the fitted values.
    real_values: Union[np.ndarray, pd.Series, list]
        The array-like object containing the N real values.
    value_positive: Any
        The value in the data that corresponds to 1 in the boolean logic.
        It is generally associated with the idea of "positive" or being in
        the "treatment" group. By default is 1.
    """

    def __init__(
        self,
        real_values: Union[np.ndarray, pd.Series, list],
        fitted_values: Union[np.ndarray, pd.Series, list],
        value_positive: Any = 1,
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
        value_positive: Any
            The value in the data that corresponds to 1 in the boolean logic.
            It is generally associated with the idea of "positive" or being in
            the "treatment" group. By default is 1.
        """
        super().__init__(real_values=real_values, fitted_values=fitted_values)
        self.value_positive = value_positive

    @property
    def value_negative(self) -> Any:
        """Return the value that it is not the positive value."""
        other_only = self.real_values[self.real_values != self.value_positive]
        if isinstance(self.real_values, np.ndarray):
            return other_only[0].copy()
        return other_only.reset_index(drop=True)[0]

    @property
    def balanced_accuracy_score(self) -> float:
        """Return the float representing the arithmetic mean between recall score
        and specificity score.

        It provides an idea of the goodness of the prediction in unbalanced datasets.
        """
        from easypred.metrics import balanced_accuracy_score

        return balanced_accuracy_score(
            self.real_values, self.fitted_values, self.value_positive
        )

    @property
    def false_positive_rate(self) -> float:
        """Return the ratio between the number of false positives and the total
        number of real negatives.

        It tells the percentage of negatives falsely classified as positive."""
        from easypred.metrics import false_positive_rate

        return false_positive_rate(
            self.real_values, self.fitted_values, self.value_positive
        )

    @property
    def false_negative_rate(self):
        """Return the ratio between the number of false negatives and the total
        number of real positives.

        It tells the percentage of positives falsely classified as negative."""
        from easypred.metrics import false_negative_rate

        return false_negative_rate(
            self.real_values, self.fitted_values, self.value_positive
        )

    @property
    def recall_score(self):
        """Return the ratio between the correctly predicted positives and the
        total number of real positives.

        It measures how good the model is in detecting real positives.

        Also called: sensitivity, true positive rate, hit rate."""
        from easypred.metrics import recall_score

        return recall_score(self.real_values, self.fitted_values, self.value_positive)

    @property
    def specificity_score(self):
        """Return the ratio between the correctly predicted negatives and the
        total number of real negatives.

        It measures how good the model is in detecting real negatives.

        Also called: selectivity, true negative rate."""
        from easypred.metrics import specificity_score

        return specificity_score(
            self.real_values, self.fitted_values, self.value_positive
        )

    @property
    def precision_score(self):
        """Return the ratio between the number of correctly predicted positives
        and the total number predicted positives.

        It measures how accurate the positive predictions are.

        Also called: positive predicted value."""
        from easypred.metrics import precision_score

        return precision_score(
            self.real_values, self.fitted_values, self.value_positive
        )

    @property
    def negative_predictive_value(self):
        """Return the ratio between the number of correctly classified negative
        and the total number of predicted negative.

        It measures how accurate the negative predictions are."""
        from easypred.metrics import negative_predictive_value

        return negative_predictive_value(
            self.real_values, self.fitted_values, self.value_positive
        )

    @property
    def f1_score(self):
        """Return the harmonic mean of the precision and recall.

        It gives an idea of an overall goodness of your precision and recall taken
        together.

        Also called: balanced F-score or F-measure"""
        from easypred.metrics import f1_score

        return f1_score(self.real_values, self.fitted_values, self.value_positive)

    def confusion_matrix(
        self, relative: bool = False, as_dataframe: bool = False
    ) -> Union[np.ndarray, pd.DataFrame]:
        """Return the confusion matrix for the binary classification.

        The confusion matrix is a matrix with shape (2, 2) that classifies the
        predictions into four categories, each represented by one of its elements:
        - [0, 0] : negative classified as negative
        - [0, 1] : negative classified as positive
        - [1, 0] : positive classified as negative
        - [1, 1] : positive classified as positive

        Parameters
        ----------
        relative : bool, optional
            If True, absolute frequencies are replace by relative frequencies.
            By default False.
        as_dataframe : bool, optional
            If True, the matrix is returned as a pandas dataframe for better
            readability. Otherwise a numpy array is returned. By default False.

        Returns
        -------
        Union[np.ndarray, pd.DataFrame]
            If as_dataframe is False, return a numpy array of shape (2, 2).
            Otherwise return a pandas dataframe of the same shape.
        """
        pred_pos = self.fitted_values == self.value_positive
        pred_neg = self.fitted_values != self.value_positive
        real_pos = self.real_values == self.value_positive
        real_neg = self.real_values != self.value_positive

        conf_matrix = np.array(
            [
                [(pred_neg & real_neg).sum(), (pred_pos & real_neg).sum()],
                [(pred_neg & real_pos).sum(), (pred_pos & real_pos).sum()],
            ]
        )

        # Divide by total number of values to obtain relative frequencies
        if relative:
            conf_matrix = conf_matrix / len(self.fitted_values)

        if not as_dataframe:
            return conf_matrix
        return self._confusion_matrix_dataframe(conf_matrix)

    def _confusion_matrix_dataframe(self, conf_matrix: np.ndarray) -> pd.DataFrame:
        """Convert a numpy confusion matrix into a pandas dataframe and add
        index and columns labels."""
        conf_df = pd.DataFrame(conf_matrix)
        values = [self.value_negative, self.value_positive]
        conf_df.columns = [f"Pred {val}" for val in values]
        conf_df.index = [f"Real {val}" for val in values]
        return conf_df

    def describe(self) -> pd.DataFrame:
        """Return a dataframe containing some key information about the
        prediction."""
        basic_info = self._describe()
        new_info = pd.DataFrame(
            {
                "Recall": self.recall_score,
                "Specificity": self.specificity_score,
                "Precision": self.precision_score,
                "Negative PV": self.negative_predictive_value,
                "F1 score": self.f1_score,
            },
            index=["Value"],
        ).transpose()
        return basic_info.append(new_info)

    @classmethod
    def from_prediction(
        cls, prediction: Prediction, value_positive
    ) -> BinaryPrediction:
        """Create an instance of BinaryPrediction.

        Parameters
        ----------
        prediction : Prediction
            The prediction object the BinaryPrediction is to be constructed from.
        value_positive : Any
            The value in the data that corresponds to 1 in the boolean logic.
            It is generally associated with the idea of "positive" or being in
            the "treatment" group. By default is 1.

        Returns
        -------
        BinaryPrediction
            An object of type BinaryPrediction, a subclass of Prediction specific
            for predictions with just two outcomes.
        """
        return cls(
            fitted_values=prediction.fitted_values,
            real_values=prediction.real_values,
            value_positive=value_positive,
        )
