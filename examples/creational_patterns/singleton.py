class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DBConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.client = "db_client"

    def get_data(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        print(f"Used {self.client} for query data with object id:{id(self)}")


if __name__ == "__main__":
    # The client code.

    db_connection_1 = DBConnection()
    db_connection_2 = DBConnection()

    db_connection_1.get_data()
    db_connection_2.get_data()
