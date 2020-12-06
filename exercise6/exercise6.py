from functools import reduce
from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return file.read().split("\n\n")


def get_answers(people: str) -> int:
    return len(set(people.replace("\n", "")))


def first_exercise(data: List[str]) -> int:
    return sum(get_answers(people) for people in data)


def get_equal_answers(group: str) -> int:
    return len(reduce(set.intersection, (set(person) for person in group.split("\n"))))


def second_exercise(data: List[str]) -> int:
    return sum(get_equal_answers(group) for group in data)


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
