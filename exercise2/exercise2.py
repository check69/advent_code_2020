from typing import List, Union, Tuple, Generator
# We can use parse library for next parse data from the file


def read_file(filename: str) -> List[List[Union[int, str]]]:
    with open(filename, "r") as file:
        return [line.split() for line in file]


def split_data(data: List[str]) -> Tuple[Generator[int, None, None], str, str]:
    numbers = (int(number) for number in data[0].split("-"))
    letter = data[1][0]
    actual_password = data[2]

    return numbers, letter, actual_password


def first_policy(data: List[str]) -> bool:
    numbers, letter, password = split_data(data)

    return next(numbers) <= password.count(letter) <= next(numbers)


def first_exercise(data: List[List[Union[int, str]]]) -> int:
    return sum(1 for password in data if first_policy(password))


def second_policy(data: List[str]) -> bool:
    numbers, letter, password = split_data(data)

    first_position = password[next(numbers) - 1]
    second_position = password[next(numbers) - 1]

    return (first_position == letter) ^ (second_position == letter)


def second_exercise(data: List[List[Union[int, str]]]):
    return sum(1 for password in data if second_policy(password))


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
