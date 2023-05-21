from __future__ import annotations

from abc import ABC, abstractmethod


class ModelCreator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        raise NotImplementedError

    def run_training_process(self) -> None:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        model = self.factory_method()
        model.load_data()
        model.train_model()
        model.print_metrics()


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class NNModelCreator(ModelCreator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Model:
        return NNModel()


class DecisionTreeModelCreator(ModelCreator):
    def factory_method(self) -> Model:
        return DecisionTreeModel()


class Model(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def load_data(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def train_model(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def print_metrics(self) -> None:
        raise NotImplementedError


"""
Concrete Products provide various implementations of the Product interface.
"""


class NNModel(Model):
    def load_data(self) -> None:
        print("NN Model load data")

    def train_model(self) -> None:
        print("NN model train model")

    def print_metrics(self) -> None:
        print("NN model print metrics")


class DecisionTreeModel(Model):
    def load_data(self) -> None:
        print("Decision Tree Model load data")

    def train_model(self) -> None:
        print("Decision Tree model train model")

    def print_metrics(self) -> None:
        print("Decision Tree model print metrics")


def client_code(creator: ModelCreator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    creator.run_training_process()


if __name__ == "__main__":
    print("Used NN model")
    client_code(NNModelCreator())
    print("\n")

    print("Used Decision tree model")
    client_code(DecisionTreeModelCreator())

# output:
# Used NN model
# NN Model load data
# NN model train model
# NN model print metrics


# Used Decision tree model
# Decision Tree Model load data
# Decision Tree model train model
# Decision Tree model print metrics
