from typing import List


FileData = List[str]


def read_file(filename: str) -> FileData:
    with open(filename, "r") as file:
        return file.readlines()


def first_exercise(data: FileData) -> int:
    return 0


def second_exercise(data: FileData) -> int:
    return 0


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
