import itertools
from copy import deepcopy
from typing import List, Tuple, Generator, Callable, Dict, Optional


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return [line.strip("\n") for line in file]


def pair_is_not_zero(pair) -> bool:
    return pair[0] != 0 or pair[1] != 0


def get_directions() -> Generator[Tuple[int, int], None, None]:
    return (pair for pair in itertools.product((1, 0, -1), (1, 0, -1)) if pair_is_not_zero(pair))


def get_adjacent_positions_base(row: int, column: int,
                                seats: List[str]) -> Generator[Tuple[int, int], None, None]:
    length_row = len(seats)
    length_column = len(seats[row])
    return (
        (r, c) for x, y in get_directions() if (
            (0 <= (r := row + x) < length_row) and
            (0 <= (c := column + y) < length_column) and
            (r, c) != (row, column))
    )


def get_next_seat(pos_x: int, dir_x: int, length_plane: int,
                  pos_y: int, dir_y: int, length_rows: int, seats: List[str]) -> Optional[Tuple[int, int]]:
    while 0 <= pos_x + dir_x < length_plane and 0 <= pos_y + dir_y < length_rows:
        pos_x += dir_x
        pos_y += dir_y
        if seats[pos_x][pos_y] != ".":
            return pos_x, pos_y

    return None


def get_adjacent_positions_advance(x: int, y: int, seats: List[str]) -> List[Tuple[int, int]]:
    length_plane = len(seats)
    length_rows = len(seats[x])

    return [
        position for dir_x, dir_y in get_directions()
        if (position := get_next_seat(x, dir_x, length_plane, y, dir_y, length_rows, seats)) is not None
    ]


def check_adjacent_places(seats: List[str], checkers: Generator[Tuple[int, int], None, None]) -> bool:
    return all(seats[row][column] != OCCUPIED_SPOT for row, column in checkers)


def first_condition(seats: List[str], checkers: Generator[Tuple[int, int], None, None], *_args) -> str:
    return OCCUPIED_SPOT if check_adjacent_places(seats, checkers) is True else FREE_SPOT


def second_condition(seats: List[str], checkers: Generator[Tuple[int, int], None, None],
                     tolerant_value: int, *_args) -> str:
    counter = sum(1 for x, y in checkers if seats[x][y] == OCCUPIED_SPOT)
    return FREE_SPOT if counter >= tolerant_value else OCCUPIED_SPOT


FREE_SPOT: str = "L"
OCCUPIED_SPOT: str = "#"
CONDITIONS = {
    FREE_SPOT: first_condition,
    OCCUPIED_SPOT: second_condition,
}


def get_place_state(row: int, column: int, seats: List[str],
                    checkers: Generator[Tuple[int, int], None, None], *args) -> str:
    if (function := CONDITIONS.get(seats[row][column])) is not None:
        return function(seats, checkers, *args)

    return seats[row][column]


def organizing_people_in_seats_system(seats: List[str], calc_adjacent_places: Callable,
                                      tolerant_value: int) -> List[str]:
    return ["".join(get_place_state(row, column, seats,
                                    calc_adjacent_places(row, column, seats), tolerant_value)
                    for column in range(len(seats[row])))
            for row in range(len(seats))]


def compare_seats(old_seats: List[str], new_seats: List[str]) -> bool:
    return any(x != y for x, y in zip(old_seats, new_seats))


def count_occupied_seats(seats: List[str], calc_adjacent_places: Callable, tolerant_value: int) -> int:
    old_seats = deepcopy(seats)
    while True:
        new_seats_distribution = organizing_people_in_seats_system(old_seats, calc_adjacent_places, tolerant_value)
        if compare_seats(old_seats, new_seats_distribution) is False:
            return sum(row.count(OCCUPIED_SPOT) for row in old_seats)

        old_seats = deepcopy(new_seats_distribution)


def first_exercise(data: List[str]) -> int:
    return count_occupied_seats(data, get_adjacent_positions_base, 4)


def second_exercise(data: List[str]) -> int:
    return count_occupied_seats(data, get_adjacent_positions_advance, 5)


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
