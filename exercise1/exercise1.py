import itertools
from typing import List, Generator


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()


def get_data(filename: str) -> List[int]:
    return [int(i) for i in read_file(filename)]


def first_exercise(data: List[int]) -> Generator[int, None, None]:
    return (x * y for x, y in itertools.product(data, data) if x + y == 2020)


def second_exercise(data: List[int]) -> Generator[int, None, None]:
    return (x * y * z for x, y, z in itertools.product(data, data, data) if x + y + z == 2020)


def main():
    data : List[int] = get_data("data1")
    print("The result of the first exercise is: ", next(first_exercise(data)))
    print("The result of the second exercise is: ", next(second_exercise(data)))


if __name__ == "__main__":
    main()
