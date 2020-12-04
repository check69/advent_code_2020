from typing import List
import re


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return file.read().split("\n\n")


def is_valid_passport(passport: str) -> bool:
    valid_fields = ("ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:")
    return all(field in passport for field in valid_fields)


"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""
byr = "byr:(19[2-9][0-9]|200[0-2]){1}"
iyr = "iyr:(20(1[0-9]|20)){1}"
eyr = "eyr:(20(2[0-9]|30)){1}"
hgt = "hgt:((1([5-8][0-9]|9[0-3])cm)|(59|6[0-9]|7[0-6])in){1}"
hcl = "hcl:#([0-9a-f]{6}){1}"
ecl = "ecl:(amb|blu|brn|gry|grn|hzl|oth){1}"
pid = "pid:([0-9]{9})"
REGEX = (byr, iyr, eyr, hgt, hcl, ecl, pid)


def is_fields_valid(passport: str) -> bool:
    if all(re.search(pattern, passport) for pattern in REGEX):
        print("------------")
        print(passport)
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
