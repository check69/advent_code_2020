from typing import List, Tuple, Callable, Dict
import parse


def parse_lines(line: str) -> Tuple[str, int]:
    fmt_str = "{operation} {argument}"
    matches = parse.parse(fmt_str, line)
    return matches["operation"], int(matches["argument"])


def read_file(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return [parse_lines(line) for line in file]


def nop(argument: int, current_instruction: int, accumulator: int) -> Tuple[int, int]:
    return jmp(1, current_instruction, accumulator)


def jmp(argument: int, current_instruction: int, accumulator: int) -> Tuple[int, int]:
    return current_instruction + argument, accumulator


def acc(argument: int, current_instruction: int, accumulator: int) -> Tuple[int, int]:
    return current_instruction + 1, accumulator + argument


operations = {
    "nop": nop,
    "jmp": jmp,
    "acc": acc
}


def run_program(instructions: List[Tuple[str, int]], operations: Dict[str, Callable]) -> Tuple[int, int]:
    accumulator = 0
    instruction_already_executed = []
    current_instruction = 0
    while current_instruction not in instruction_already_executed and current_instruction < len(instructions):
        instruction_already_executed.append(current_instruction)
        current_instruction, accumulator = operations[instructions[current_instruction][0]](
            instructions[current_instruction][1], current_instruction, accumulator)

    return accumulator, current_instruction


def change_instruction(instruction: Tuple[str, int]) -> Tuple[bool, Tuple[str, int], Tuple[str, int]]:
    if instruction[0] == "nop":
        if instruction[1] != 0:
            return True, instruction, ("jmp", instruction[1])
    elif instruction[0] == "jmp":
        return True, instruction, ("nop", instruction[1])

    return False, instruction, instruction


def brute_force_to_find_the_error(instructions: List[Tuple[str, int]], operations: Dict[str, Callable]) -> int:
    for instruction_pos in range(len(instructions)):
        is_change, old_instruction, new_instruction = change_instruction(instructions[instruction_pos])

        if is_change is False:
            continue

        instructions[instruction_pos] = new_instruction

        accumulator, current_instruction = run_program(instructions, operations)
        if current_instruction >= len(instructions):
            return accumulator

        instructions[instruction_pos] = old_instruction

    return 0


def first_exercise(data: List[Tuple[str, int]]) -> int:
    return run_program(data, operations)[0]


def second_exercise(data: List[str]) -> int:
    return brute_force_to_find_the_error(data, operations)


def main():
    data = read_file("data")
    print("The result of the first exercise is: ", first_exercise(data))
    print("The result of the second exercise is: ", second_exercise(data))


if __name__ == "__main__":
    main()
