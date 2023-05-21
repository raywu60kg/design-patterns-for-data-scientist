from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

import numpy as np
from sklearn import preprocessing


class ContinuousVariableFeatureEngineering:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def process(self, data: np.array) -> np.array:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        return self._strategy.process(data)


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def process(self, data: List):
        raise NotImplementedError


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class Normalize(Strategy):
    def process(self, data: np.array) -> np.array:
        return preprocessing.Normalizer().fit(data)


class Standardize(Strategy):
    def process(self, data: np.array) -> np.array:
        return preprocessing.StandardScaler().fit(data)


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.
    data = np.array([[1.0, -1.0, 2.0], [2.0, 0.0, 0.0], [0.0, 1.0, -1.0]])
    context = ContinuousVariableFeatureEngineering(Normalize())
    print("Client: Strategy is Normalize")
    print(context.process(data))
    print()

    print("Client: Strategy is Standardize")
    context.strategy = Standardize()
    print(context.process(data))
