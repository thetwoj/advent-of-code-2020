def group_answers(inputs):
    answers = []
    current_group = set()
    for line in inputs:
        if line == "":
            answers.append(current_group)
            current_group = set()
            continue
        for answer in line:
            current_group.add(answer)
    answers.append(current_group)
    return answers


def unanimous_answers(inputs):
    # Doing this with set intersections would have been easier
    # since that's effectively what I manually implemented
    answers = []
    current_group = set()
    next_first = True
    for line in inputs:
        if line == "":
            answers.append(current_group)
            current_group = set()
            next_first = True
            continue

        if next_first:
            for answer in line:
                current_group.add(answer)
        else:
            to_remove = []
            for answer in current_group:
                if answer not in line:
                    to_remove.append(answer)
            for answer in to_remove:
                current_group.remove(answer)
        next_first = False
    answers.append(current_group)
    return answers


def get_input():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    inputs = get_input()
    grouped_answers = group_answers(inputs)
    answer_sum = 0
    for group in grouped_answers:
        answer_sum += len(group)
    print(f"{answer_sum} questions were asked across all groups")

    print("-" * 20)
    # part 2
    unanimous = unanimous_answers(inputs)
    unanimous_answer_sum = 0
    for group in unanimous:
        unanimous_answer_sum += len(group)
    print(f"{unanimous_answer_sum} questions were asked across all groups")
