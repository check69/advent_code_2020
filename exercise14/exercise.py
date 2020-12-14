import itertools
from typing import List, Dict, Tuple

import parse

FileData = Dict[str, Tuple[int, str]]


def parse_mask(line: str) -> str:
    return line.strip("\n")[7:]


def parse_mem(line: str) -> Tuple[int, str]:
    fmt_str = "mem[{address:d}] = {value:d}"
    matches = parse.parse(fmt_str, line)
    return matches["address"], matches["value"]


def parse_file(file: List[str]) -> FileData:
    data = {}
    current_mask = 0
    for line in file:
        if line.startswith("mask"):
            current_mask = parse_mask(line)
            data[current_mask] = []
        else:
            address, value = parse_mem(line)
            data[current_mask].append((address, value))

    return data


def read_file(filename: str) -> FileData:
    with open(filename, "r") as file:
        return parse_file(file.readlines())


def get_value_mask(value: int, mask: str) -> int:
    or_mask = int(mask.replace("X", "0"), 2)
    and_mask = int(mask.replace("X", "1"), 2)

    return (value & and_mask) | or_mask


def first_exercise(data: FileData) -> int:
    ret = {}

    for mask, memory in data.items():
        for address, value in memory:
            ret[address] = get_value_mask(value, mask)

    return sum(ret.values())


def get_x_position(mask: str) -> List[int]:
    return [position for position, bit in enumerate(mask) if bit == "X"]


def get_all_possibilities(mask: str) -> List[int]:
    x_positions = get_x_position(mask)

    ret = []
    for element in itertools.product([0, 1], repeat=len(x_positions)):
        the_mask = mask
        for position in range(len(x_positions)):
            the_mask = (f"{the_mask[:x_positions[position]]}"
                        f"{str(element[position])}{the_mask[x_positions[position] + 1:]}")

        ret.append(int(the_mask, 2))

    return ret


def get_base_address(mask: str, address: int) -> int:
    or_mask = int(mask.replace("X", "0"), 2)
    and_mask = int(mask.replace("0", "1").replace("X", "0"), 2)
    return (address | or_mask) & and_mask


def get_addresses(mask: str, address: int, mask_list: List[int]) -> List[int]:
    base_address = get_base_address(mask, address)

    return [mask_option | base_address for mask_option in mask_list]


def second_exercise(data: FileData) -> int:
    ret = {}

    for mask, memory in data.items():
        mask_list = get_all_possibilities(mask)
        for address, value in memory:
            for new_address in get_addresses(mask, address, mask_list):
                ret[new_address] = value

    return sum(ret.values())


def main():
    data = read_file("data")
    print("The result of the first exercise is:", first_exercise(data))
    print("The result of the second exercise is:", second_exercise(data))


if __name__ == "__main__":
    main()
