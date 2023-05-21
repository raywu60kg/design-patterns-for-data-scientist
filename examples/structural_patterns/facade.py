from __future__ import annotations


class Facade:
    """
    The Facade class provides a simple interface to the complex logic of one or
    several subsystems. The Facade delegates the client requests to the
    appropriate objects within the subsystem. The Facade is also responsible for
    managing their lifecycle. All of this shields the client from the undesired
    complexity of the subsystem.
    """

    def __init__(self, subsystem1: ModelTraining, subsystem2: Notification) -> None:
        """
        Depending on your application's needs, you can provide the Facade with
        existing subsystem objects or force the Facade to create them on its
        own.
        """

        self._subsystem1 = subsystem1 or ModelTraining()
        self._subsystem2 = subsystem2 or Notification()

    def operation(self) -> str:
        """
        The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only to a fraction
        of a subsystem's capabilities.
        """

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem2.notify_user())
        results.append(self._subsystem1.get_data())
        results.append(self._subsystem1.train_model())
        results.append(self._subsystem2.update_training_status())
        return "\n".join(results)


class ModelTraining:
    """
    The Subsystem can accept requests either from the facade or client directly.
    In any case, to the Subsystem, the Facade is yet another client, and it's
    not a part of the Subsystem.
    """

    def get_data(self) -> str:
        return "Get data"

    # ...

    def train_model(self) -> str:
        return "Train model"


class Notification:
    """
    Some facades can work with multiple subsystems at the same time.
    """

    def notify_user(self) -> str:
        return "Notify user"

    # ...

    def update_training_status(self) -> str:
        return "Update training status"


def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """

    print(facade.operation())


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = ModelTraining()
    subsystem2 = Notification()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
    # output:
    # Facade initializes subsystems:
    # Notify user
    # Get data
    # Train model
    # Update training status
