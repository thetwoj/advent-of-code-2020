def fix_program(instructions, acc, breadcrumbs):

    while True:
        index, tup = breadcrumbs.pop()
        instruction, value = tup
        if instruction == "acc":
            acc -= value
        elif instruction == "nop":
            result = run_until_success(
                instructions, breadcrumbs, acc, index, ("jmp", value)
            )
            if result:
                return result
            index -= 1
        elif instruction == "jmp":
            result = run_until_success(
                instructions, breadcrumbs, acc, index, ("nop", value)
            )
            if result:
                return result


def run_until_success(instructions, breadcrumbs, acc, index, first_instruction):
    seen = {i for i, _ in breadcrumbs}
    instruction, value = first_instruction

    try:
        while index not in seen:
            seen.add(index)
            if instruction == "nop":
                index += 1
                instruction, value = instructions[index]
            elif instruction == "acc":
                acc += value
                index += 1
                instruction, value = instructions[index]
            elif instruction == "jmp":
                index += value
                instruction, value = instructions[index]

        return False
    except IndexError as _:
        return acc


def run_until_repeat(instructions):
    acc = 0
    index = 0
    seen = set()
    instruction, value = instructions[0]
    breadcrumbs = []

    while index not in seen:
        seen.add(index)
        breadcrumbs.append((index, instructions[index]))
        if instruction == "nop":
            index += 1
            instruction, value = instructions[index]
        elif instruction == "acc":
            acc += value
            index += 1
            instruction, value = instructions[index]
        elif instruction == "jmp":
            index += value
            instruction, value = instructions[index]

    return acc, breadcrumbs


def extract_instructions(inputs):
    instructions = []
    for line in inputs:
        instruction, value = line.split(" ")
        value = int(value)
        instructions.append((instruction, value))
    return instructions


def get_input():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    inputs = get_input()
    instructions = extract_instructions(inputs)
    acc_before_repeat, breadcrumbs = run_until_repeat(instructions)
    print(f"{acc_before_repeat} was the acc value prior to repeating")

    print("-" * 20)
    # part 2
    acc_after_success = fix_program(instructions, acc_before_repeat, breadcrumbs)
    print(f"{acc_after_success} was the acc value after successful execution")
