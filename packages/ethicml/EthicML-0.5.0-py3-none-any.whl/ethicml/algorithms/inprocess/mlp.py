"""Wrapper for SKLearn implementation of MLP."""
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd
from ranzen import implements
from sklearn.neural_network import MLPClassifier

from ethicml.utility import ActivationType, DataTuple, Prediction, TestTuple

from .in_algorithm import InAlgorithm

__all__ = ["MLP"]


ACTIVATIONS: Dict[str, ActivationType] = {
    "identity": "identity",
    "logistic": "logistic",
    "tanh": "tanh",
    "relu": "relu",
}


class MLP(InAlgorithm):
    """Multi-layer Perceptron."""

    def __init__(
        self,
        hidden_layer_sizes: Optional[Tuple[int]] = None,
        activation: Optional[ActivationType] = None,
        seed: int = 888,
    ):
        super().__init__(name="MLP", is_fairness_algo=False, seed=seed)
        if hidden_layer_sizes is None:
            self.hidden_layer_sizes = MLPClassifier().hidden_layer_sizes
        else:
            self.hidden_layer_sizes = hidden_layer_sizes
        self.activation: ActivationType = (
            MLPClassifier().activation if activation is None else activation
        )

    @implements(InAlgorithm)
    def fit(self, train: DataTuple) -> InAlgorithm:
        self.clf = select_mlp(self.hidden_layer_sizes, self.activation, seed=self.seed)
        self.clf.fit(train.x, train.y.to_numpy().ravel())
        return self

    @implements(InAlgorithm)
    def predict(self, test: TestTuple) -> Prediction:
        return Prediction(hard=pd.Series(self.clf.predict(test.x)))

    @implements(InAlgorithm)
    def run(self, train: DataTuple, test: TestTuple) -> Prediction:
        clf = select_mlp(self.hidden_layer_sizes, self.activation, seed=self.seed)
        clf.fit(train.x, train.y.to_numpy().ravel())
        return Prediction(hard=pd.Series(clf.predict(test.x)))


def select_mlp(
    hidden_layer_sizes: Tuple[int], activation: ActivationType, seed: int
) -> MLPClassifier:
    """Create MLP model for the given parameters."""
    assert activation in ACTIVATIONS

    random_state = np.random.RandomState(seed=seed)
    return MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes, activation=activation, random_state=random_state
    )
