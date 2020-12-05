from functools import reduce
from typing import List, Tuple


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return [line.strip() for line in file]


def calculate_half(boarding_pass_row: str, min_row: int, max_row: int) -> Tuple[int]:
    row = (min_row + max_row) / 2
    if boarding_pass_row in "FL":
        max_row = row if isinstance(row, int) else int(row - 0.5)
    else:
        min_row = row if isinstance(row, int) else int(row + 0.5)

    return min_row, max_row


def get_position(boarding_pass: str, min_row: int, max_row: int) -> int:
    return min(reduce(lambda x, letter: calculate_half(letter, *x), boarding_pass, (min_row, max_row)))


def get_seat_id(boarding_pass: str) -> int:
    return 8 * get_position(boarding_pass[:7], 0, 127) + get_position(boarding_pass[7:], 0, 7)


def get_sorted_seats_id(data: List[str]) -> List[int]:
    return sorted([get_seat_id(boarding_pass) for boarding_pass in data])


def first_exercise(data: List[str]) -> int:
    return max(get_seat_id(boarding_pass) for boarding_pass in data)


def get_missing_boarding_pass(sorted_list: List[int]) -> int:
    return set(range(sorted_list[0], sorted_list[-1])).difference(set(sorted_list)).pop()


def second_exercise(data: List[str]) -> int:
    return get_missing_boarding_pass(get_sorted_seats_id(data))


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
