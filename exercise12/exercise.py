from typing import List, Tuple


FileData = List[Tuple[str, int]]


def parse_lines(line: str) -> Tuple[str, int]:
    return line[0], int(line[1:])


def read_file(filename: str) -> FileData:
    with open(filename, "r") as file:
        return [parse_lines(line) for line in file]


def get_rotation(degrees: int) -> int:
    return degrees // 90


def get_direction(rotation_side: str, degrees: int, current_rotation: int) -> int:
    rotation = get_rotation(degrees)
    if rotation_side == "L":
        rotation = -rotation

    return (current_rotation + rotation) % 4


DIRECTIONS = {"N": 0, "E": 1, "S": 2, "W": 3}


def first_exercise(data: FileData) -> int:
    movement = [0, 0, 0, 0]
    direction = 1
    for command, value in data:
        if command in "LR":
            direction = get_direction(command, value, direction)
        elif command == "F":
            movement[direction] += value
        elif command in "NESW":
            movement[DIRECTIONS[command]] += value

    return abs(movement[0] - movement[2]) + abs(movement[1] - movement[3])


def calc_rotation(command: str, degrees: int) -> int:
    rotation = degrees // 90
    if command == "L":
        return (-rotation) % 4

    return rotation


def move_waypoint(command: str, degrees: int, waypoint: List[int]) -> List[int]:
    rotation = calc_rotation(command, degrees)
    return waypoint[-rotation:] + waypoint[:-rotation]


def second_exercise(data: FileData) -> int:
    waypoint = [1, 10, 0, 0]
    east = 0
    north = 0
    for letter, value in data:
        if letter in "LR":
            waypoint = move_waypoint(letter, value, waypoint)
        elif letter == "F":
            north += value * (waypoint[0] - waypoint[2])
            east += value * (waypoint[1] - waypoint[3])
        elif letter in "NEWS":
            waypoint[DIRECTIONS[letter]] += value

    return abs(north) + abs(east)


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
