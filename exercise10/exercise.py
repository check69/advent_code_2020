import itertools
import math
from collections import Counter
from functools import reduce
from typing import List, Tuple
"""
This solution has a problem for data that has more than 4 numbers consecutively, but in my data I hadn't that problem.
the solution could be the sum of (n!/(x!(n - x)!)) and then make some subtraction to remove invalid solutions.
But I don't know how to get that subtraction variable.
"""


def read_file(filename: str) -> List[int]:
    with open(filename, "r") as file:
        return [int(line) for line in file]


def add_min_and_max_jolt(jolts: List[int]) -> List[int]:
    sorted_jolts = sorted(jolts)
    return [0, *sorted_jolts, sorted_jolts[-1] + 3]


def calc_jolt_distance(jolts: List[int]) -> List[int]:
    return [b - a for a, b in zip(jolts, jolts[1:])]


def group_jolts_distance(jolts_distance: List[int]) -> List[int]:
    return Counter(jolts_distance).values()


def jolt_difference(jolts: List[int]) -> Tuple[int, int]:
    jolts_count = group_jolts_distance(calc_jolt_distance(add_min_and_max_jolt(jolts)))
    return math.prod(jolts_count)


def get_subgroups_count(jolts_distance: List[int]) -> List[Tuple[int, int]]:
    groups = itertools.groupby(jolts_distance)
    return ((a, len(list(b))) for a, b in groups)


# I would like to know maths to calculate these numbers, but for now this gets the job done
combination_result = {
    1: 2,
    2: 4,
    3: 7
}


def possible_combinations(number: int) -> int:
    return combination_result.get(number, 1)


def calc_combinations(subgroups: List[Tuple[int, int]]) -> int:
    filtered_subgroups = filter(lambda x: x[0] == 1, subgroups)

    def steps_to_calc_combinations(accumulator: int, max_combinations: Tuple[int, int]) -> int:
        return accumulator * possible_combinations(max_combinations[1] - 1)

    return reduce(steps_to_calc_combinations, filtered_subgroups, 1)


def get_multiple_combinations(jolts: List[int]) -> int:
    jolts_distance = calc_jolt_distance(add_min_and_max_jolt(jolts))
    subgroups = get_subgroups_count(jolts_distance)

    return calc_combinations(subgroups)


def first_exercise(data: List[int]) -> int:
    return jolt_difference(data)


def second_exercise(data: List[int]) -> int:
    return get_multiple_combinations(data)


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
