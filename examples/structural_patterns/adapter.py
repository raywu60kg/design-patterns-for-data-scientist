from typing import List


class DataLoader:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def get_train_data(self) -> List[int]:
        return [0, 1, 2]

    def get_val_data(self) -> List[int]:
        return [3, 4, 5]

    def get_test_data(self) -> List[int]:
        return [6, 7, 8]


class AdapteeDataLoader:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def get_all_data(self) -> str:
        return [0, 1, 2, 3, 4, 5, 6, 7, 8]


class Adapter(DataLoader):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via composition.
    """

    def __init__(self, adaptee: AdapteeDataLoader) -> None:
        self.adaptee = adaptee
        self.all_data = adaptee.get_all_data()

    def get_train_data(self) -> List[int]:
        return self.all_data[:3]

    def get_val_data(self) -> List[int]:
        return self.all_data[3:6]

    def get_test_data(self) -> List[int]:
        return self.all_data[6:9]


def client_code(target: DataLoader) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print("train data: ", target.get_train_data())
    print("val data:   ", target.get_val_data())
    print("test data:  ", target.get_test_data())


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = DataLoader()
    client_code(target)
    print("\n")

    adaptee = AdapteeDataLoader()
    print(
        "Client: The Adaptee class has a weird interface. "
        "See, I don't understand it:"
    )
    print(f"Adaptee: {adaptee.get_all_data()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
