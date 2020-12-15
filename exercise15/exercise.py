from typing import List, Dict

FileData = List[int]


def initial_dictionary(data: FileData) -> Dict[int, int]:
    return {
        number: position
        for position, number in enumerate(data, 1)
    }


def get_new_number(iteration: int, previous_number: int, numbers_position: Dict[int, int]) -> int:
    if previous_number not in numbers_position:
        numbers_position[previous_number] = iteration
        return 0

    new_number = iteration - numbers_position[previous_number]
    numbers_position[previous_number] = iteration

    return new_number


def solve(data: FileData, iterations: int) -> int:
    numbers_position = initial_dictionary(data[:-1])

    previous_number = data[-1]

    for iteration in range(len(data), iterations):
        previous_number = get_new_number(iteration, previous_number, numbers_position)

    return previous_number


def first_exercise(data: FileData) -> int:
    return solve(data, 2020)


def second_exercise(data: FileData) -> int:
    return solve(data, 30000000)


def main():
    initial_list = [10, 16, 6, 0, 1, 17]
    print("The result of the first exercise is: ", first_exercise(initial_list))
    print("The result of the second exercise is: ", second_exercise(initial_list))


if __name__ == "__main__":
    main()
