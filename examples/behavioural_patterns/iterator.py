import os
from collections.abc import Iterator

import pandas as pd

"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""


class MultipleCSVIterator(Iterator):
    def __init__(self, csv_files_dir: str) -> None:
        self._files_list = []
        for file in os.listdir(csv_files_dir):
            self._files_list.append(os.path.join(csv_files_dir, file))
        self._row_idx = 0
        self._file_idx = 0
        self._table = pd.read_csv(self._files_list[self._file_idx])

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        try:
            if self._row_idx >= len(self._table):
                if self._file_idx == len(self._files_list) - 1:
                    raise StopIteration()

                # change to next table
                self._file_idx += 1
                self._table = pd.read_csv(self._files_list[self._file_idx])
                self._row_idx = 0

            value = self._table["column"][self._row_idx]
            self._row_idx += 1
        except IndexError:
            raise StopIteration()

        return value


if __name__ == "__main__":
    my_iterator = MultipleCSVIterator("./data")
    for value in my_iterator:
        print(value)
