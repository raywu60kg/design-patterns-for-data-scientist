from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ModelPipelineBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_dataloader(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_model_training(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_model_saver(self) -> None:
        raise NotImplementedError


class MyModelPipelineBuilder(ModelPipelineBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        print("Reset pipeline")
        self._product = ModelPipeline()

    @property
    def product(self) -> ModelPipeline:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def add_dataloader(self) -> None:
        self._product.add("My Dataloader")

    def add_model_training(self) -> None:
        self._product.add("My Model Training")

    def add_model_saver(self) -> None:
        self._product.add("My Model Saver")


class ModelPipeline:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def run(self) -> None:
        print(f"Run parts: {', '.join(self.parts)}")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> ModelPipelineBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ModelPipelineBuilder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_testing_pipeline(self) -> None:
        self.builder.add_dataloader()
        self.builder.add_model_training()

    def build_full_pipeline(self) -> None:
        self.builder.add_dataloader()
        self.builder.add_model_training()
        self.builder.add_model_saver()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = MyModelPipelineBuilder()
    director.builder = builder

    print("Standard basic product: ")
    director.build_testing_pipeline()
    builder.product.run()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_pipeline()
    builder.product.run()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.add_model_saver()
    builder.product.run()
    # output:
    # Reset pipeline
    # Standard basic product:
    # Reset pipeline
    # Run parts: My Dataloader, My Model Training

    # Standard full featured product:
    # Reset pipeline
    # Run parts: My Dataloader, My Model Training, My Model Saver

    # Custom product:
    # Reset pipeline
    # Run parts: My Model Saver
