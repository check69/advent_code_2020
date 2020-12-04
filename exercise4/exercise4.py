from typing import List
import re


VALID_FIELDS = ("ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:")
REGEX = ("byr:19[2-9][0-9]|200[0-2]\\b",
         "iyr:20(1[0-9]|20)\\b",
         "eyr:20(2[0-9]|30)\\b",
         "hgt:((1([5-8][0-9]|9[0-3])cm)|(59|6[0-9]|7[0-6])in)\\b",
         "hcl:#([0-9a-f]{6})\\b",
         "ecl:(amb|blu|brn|gry|grn|hzl|oth)\\b",
         "pid:([0-9]{9})\\b")


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return file.read().split("\n\n")


def is_valid_passport(passport: str) -> bool:
    return all(field in passport for field in VALID_FIELDS)


def is_fields_valid(passport: str) -> bool:
    return all(re.search(pattern, passport) for pattern in REGEX)


def get_passports(data: List[str]) -> int:
    return sum(1 for passport in data if is_valid_passport(passport))


def first_exercise(data: List[str]) -> int:
    return get_passports(data)


def second_exercise(data: List[str]) -> int:
    return sum(1 for passport in data if is_fields_valid(passport))


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
