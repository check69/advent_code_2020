from typing import List, Union, Tuple, Generator


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()


def get_password_elements(data: List[str]) -> List[List[Union[int, str]]]:
    return [elements.split() for elements in data]


def split_data(data: List[str]) -> Tuple[Generator[int, None, None], str, str]:
    numbers = (int(number) for number in data[0].split("-"))
    letter = data[1][0]
    actual_password = data[2]

    return numbers, letter, actual_password


def first_policy(data: List[str]) -> bool:
    numbers, letter, password = split_data(data)

    times = len(password.split(letter)) - 1
    if next(numbers) <= times <= next(numbers):
        return True

    return False


def first_exercise(data: List[List[Union[int, str]]]) -> int:
    return sum(1 for password in data if first_policy(password))


def second_policy(data: List[str]) -> bool:
    numbers, letter, password = split_data(data)

    first_position = password[next(numbers) - 1]
    second_position = password[next(numbers) - 1]

    if (first_position == letter or second_position == letter) and first_position != second_position:
        return True

    return False


def second_exercise(data: List[List[Union[int, str]]]):
    return sum(1 for password in data if second_policy(password))


def main():
    data = get_password_elements(read_file("data"))
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
