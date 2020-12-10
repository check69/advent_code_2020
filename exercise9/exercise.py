from typing import List


def read_file(filename: str) -> List[int]:
    with open(filename, "r") as file:
        return [int(line) for line in file]


def is_this_number_ok(number: int, preamble: List[int]) -> bool:
    for x in preamble:
        for y in preamble:
            if x != y:
                if x + y == number:
                    return True

    return False


def find_the_number_with_preamble(preamble: int, numbers: List[int]) -> int:
    start_pos = 0
    end_pos = preamble
    for position in range(preamble, len(numbers)):
        if not is_this_number_ok(numbers[position], numbers[start_pos:end_pos]):
            return numbers[position]
        start_pos += 1
        end_pos += 1


def find_the_invalid_number(invalid_number: int, numbers: List[int]) -> List[int]:
    start_pos = 0
    for end_pos in range(start_pos + 1, len(numbers)):
        while (total := sum(numbers[start_pos:end_pos])) > invalid_number:
            start_pos += 1

        if total == invalid_number:
            return numbers[start_pos:end_pos]


def first_exercise(data: List[int]) -> int:
    return find_the_number_with_preamble(25, data)


def second_exercise(data: List[int]) -> int:
    ret = find_the_invalid_number(first_exercise(data), data)
    return min(ret) + max(ret)


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
