import itertools
from typing import List, Generator


def read_file(filename: str) -> List[int]:
    with open(filename, "r") as file:
        return [int(line) for line in file]


def first_exercise(data: List[int]) -> Generator[int, None, None]:
    return (x * y for x, y in itertools.product(data, data) if x + y == 2020)


def second_exercise(data: List[int]) -> Generator[int, None, None]:
    return (x * y * z for x, y, z in itertools.product(data, data, data) if x + y + z == 2020)


def main():
    data: List[int] = read_file("data1")
    print("The result of the first exercise is: ", next(first_exercise(data)))
    print("The result of the second exercise is: ", next(second_exercise(data)))


if __name__ == "__main__":
    main()
