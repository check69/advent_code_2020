import math
from typing import List, Optional, Dict, Tuple, Set

import parse

FileData = Tuple[Dict[str, Tuple[Tuple[int, int], Tuple[int, int]]], List[int], List[int]]
string = "{key}: {value1:d}-{value2:d} or {value3:d}-{value4:d}"


def parse_line(line: str) -> Optional[Dict[str, Tuple[Tuple[int, int], Tuple[int, int]]]]:
    if line_parsed := parse.parse(string, line):
        return {line_parsed["key"]: [(line_parsed["value1"], line_parsed["value2"]),
                                     (line_parsed["value3"], line_parsed["value4"])]}


def parse_ticket_data(file) -> Dict[str, Tuple[Tuple[int, int]]]:
    ticket_data = {}
    while (line := next(file)) != "\n":
        ticket_data.update(parse_line(line))

    return ticket_data


def parse_client_tickets(file) -> List[int]:
    return list(map(int, next(file).strip().split(",")))


def parse_nearby_tickets(file) -> List[List[int]]:
    return [list(map(int, line.strip().split(","))) for line in file]


def parse_file(file) -> FileData:
    ticket_data = parse_ticket_data(file)
    next(file)
    your_ticket = parse_client_tickets(file)
    next(file)
    next(file)
    nearby_tickets = parse_nearby_tickets(file)

    return ticket_data, your_ticket, nearby_tickets


def read_file(filename: str) -> FileData:
    with open(filename, "r") as file:
        return parse_file(file)


def is_valid_ticket(value: int, possible_values: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:
    return (possible_values[0][0] <= value <= possible_values[0][1] or
            possible_values[1][0] <= value <= possible_values[1][1])


def get_invalid_tickets(data: FileData) -> List[int]:
    ticket_data, _, nearby_tickets = data

    invalid = []
    for tickets in nearby_tickets:
        for value in tickets:
            if any(is_valid_ticket(value, v) for v in ticket_data.values()):
                continue
            invalid.append(value)
    return invalid


def first_exercise(data: FileData) -> int:
    ticket_data, _, nearby_tickets = data
    invalid = get_invalid_tickets(data)

    return sum(invalid)


def get_positions(data: FileData, invalid_tickets: List[int]) -> Dict[str, Set[int]]:
    ticket_data, _, nearby_tickets = data

    positions = {k: set() for k in ticket_data}

    for tickets in nearby_tickets:
        for position, value in enumerate(tickets):
            if value not in invalid_tickets:
                for k, v in ticket_data.items():
                    if (value < v[0][0] or value > v[0][1]) and (value < v[1][0] or value > v[1][1]):
                        positions[k].add(position)

    return positions


def get_final_positions(positions: Dict[str, Set[int]]) -> Dict[str, Set[int]]:
    final_positions = {k: set() for k in positions}

    all_numbers = set(range(0, 20))
    while len(all_numbers) > 0:
        for k, v in positions.items():
            difference = all_numbers - v
            if len(difference) == 1:
                final_positions[k] = difference
                all_numbers -= difference
                break

    return final_positions


def get_specific_value(your_ticket: List[int], positions: Dict[str, Set[int]], label: str) -> List[int]:
    return [your_ticket[next(iter(v))] for k, v in positions.items() if k.startswith(label)]


def second_exercise(data: FileData) -> int:
    ticket_data, your_tickets, nearby_tickets = data
    invalid_tickets = get_invalid_tickets(data)

    positions = get_positions(data, invalid_tickets)
    final_positions = get_final_positions(positions)

    departure_values = get_specific_value(your_tickets, final_positions, "departure")
    return math.prod(departure_values)


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
