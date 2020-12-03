from functools import reduce
from operator import mul
from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()


def strip_newlines(data: List[str]) -> List[str]:
    return [line.strip() for line in data]


def getting_trees(slope: List[str], move_right: int, move_down: int) -> int:
    starting_list = 0
    starting_pos = 0

    total_trees = 0

    while starting_list + move_down < len(slope):
        starting_list += move_down
        starting_pos = (move_right + starting_pos) % len(slope[starting_list])

        if slope[starting_list][starting_pos] == "#":
            total_trees += 1

    return total_trees


def first_exercise(data: List[str]) -> int:
    return getting_trees(data, 3, 1)


def second_exercise(data: List[str]) -> int:
    numbers = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(mul, map(lambda x: getting_trees(data, x[0], x[1]), numbers))


def main():
    data = strip_newlines(read_file("data"))
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
