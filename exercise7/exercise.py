from functools import lru_cache
from typing import Dict, Tuple, Set
import parse


def split_bags(line: str) -> Tuple[str, Tuple[str]]:
    fmt_str = "{color} bags contain {children}"
    matches = parse.parse(fmt_str, line)
    return matches["color"], tuple(matches["children"].split(","))


def read_file(filename: str) -> Tuple[str]:
    with open(filename, "r") as file:
        return dict((split_bags(line) for line in file))


@lru_cache
def is_the_bag_inside(bags: Tuple[str], bag_to_find: str) -> str:
    return any(bag_to_find in bag for bag in bags)


def get_bags_inside(bag: str, data: Dict[str, Tuple[str]]) -> Set[str]:
    return set(k for k, v in data.items() if is_the_bag_inside(v, bag))


def get_all_bags_inside_a_target(data: Dict[str, Tuple[str]], target: str) -> Set[str]:
    bags = {target}
    length = 0
    while len(bags) > length:
        length = len(bags)
        bags.update(*[get_bags_inside(bag, data) for bag in bags])

    return bags


@lru_cache
def get_number_and_bag_name(bag_data: str) -> Tuple[int, str]:
    fmt_str = "{number} {bag_name}"
    matches = parse.parse(fmt_str, bag_data)
    number = int(matches["number"])
    bag_name = matches["bag_name"].split("bag")[0].strip()

    return number, bag_name


@lru_cache
def bag_has_child(bags: Tuple[str]) -> bool:
    return all("no other bag" in bag for bag in bags)


def get_count_from_bags(data: Dict[str, Tuple[str]], bags: Tuple[str]):
    if bag_has_child(tuple(bags)):
        return 0

    total = 0
    for bag in bags:
        number, bag_name = get_number_and_bag_name(bag)
        total += number + number * get_count_from_bags(data, data[bag_name])

    return total


def first_exercise(data: Dict[str, Tuple[str]]) -> int:
    return len(get_all_bags_inside_a_target(data, "shiny gold")) - 1


def second_exercise(data: Dict[str, Tuple[str]]) -> int:
    bag_name = "shiny gold"
    return get_count_from_bags(data, data[bag_name])


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
