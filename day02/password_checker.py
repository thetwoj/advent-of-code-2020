def audit_passwords_part_1(lines):
    valid_count = 0
    for line in lines:
        count, letter, password = line.split(" ")
        min = int(count.split("-")[0])
        max = int(count.split("-")[1])
        letter = letter[0]
        letter_count = len([x for x in password if x == letter])
        if min <= letter_count <= max:
            valid_count += 1

    print(f"{valid_count} valid passwords found for part 1")
    return valid_count


def audit_passwords_part_2(lines):
    valid_count = 0
    for line in lines:
        count, letter, password = line.split(" ")
        letter = letter[0]
        first = password[int(count.split("-")[0]) - 1] == letter
        second = password[int(count.split("-")[1]) - 1] == letter
        if first != second:
            valid_count += 1

    print(f"{valid_count} valid passwords found for part 2")
    return valid_count


def get_input():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    inputs = get_input()
    audit_passwords_part_1(inputs)

    print("-"*20)
    # part 2
    audit_passwords_part_2(inputs)
