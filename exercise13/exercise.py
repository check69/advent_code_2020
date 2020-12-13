import math
from typing import List, Tuple, Generator, Dict

FileData = Tuple[int, List[str]]


def parse_file(file: List[str]) -> FileData:
    return int(file[0]), file[1].strip("\n").split(",")


def read_file(filename: str) -> FileData:
    with open(filename, "r") as file:
        return parse_file(file.readlines())


def waiting_time_for_bus(estimate_time: int, bus_id: int) -> int:
    result = estimate_time / bus_id
    if result % bus_id != 0:
        result = math.trunc(result) + 1

    return result * bus_id - estimate_time


def get_closest_bus_id(estimate_time: int, bus_ids: Generator[str, None, None]) -> Tuple[int, int]:
    ret = {}
    for bus_id in bus_ids:
        bus_id = int(bus_id)
        ret[waiting_time_for_bus(estimate_time, bus_id)] = bus_id

    return ret[min(ret.keys())], min(ret.keys())


def first_exercise(data: FileData) -> int:
    estimate_time, bus_ids = data

    return math.prod(get_closest_bus_id(estimate_time, filter(lambda x: x != "x", bus_ids)))


def get_offset(bus_ids: List[str]) -> Dict[int, int]:
    ret = {}
    for offset in range(len(bus_ids)):
        bus_id = bus_ids[offset]
        if bus_id != "x":
            ret[int(bus_id)] = -offset

    return ret


###################################################################
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    total = 0
    prod = math.prod(n)

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p

    return total % prod


def mul_inv(a, b):
    if b == 1:
        return 1

    b0 = b
    x0, x1 = 0, 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0

    return x1
###################################################################


def get_bus_offset(bus_ids: List[str]) -> int:
    bus_offset = get_offset(bus_ids)
    return chinese_remainder(bus_offset.keys(), bus_offset.values())


def second_exercise(data: FileData) -> int:
    return get_bus_offset(data[1])


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
