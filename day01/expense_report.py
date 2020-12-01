def find_two_expenses_that_sum(expenses):
    expenses.sort()
    low = 0
    high = len(expenses) - 1
    while expenses[low] + expenses[high] != 2020:
        if expenses[low] + expenses[high] > 2020:
            high -= 1
        else:
            low += 1
    print(
        "The two expenses that sum to 2020 are: %d, %d"
        % (expenses[low], expenses[high])
    )
    return expenses[low], expenses[high]


def multiply_expenses(*args):
    product = 1
    for arg in args:
        product *= arg
    print("The product of the expenses is: %d" % product)


def find_three_expenses_that_sum(expenses):
    expenses.sort()
    for exp1 in expenses:
        for exp2 in expenses[1:]:
            for exp3 in expenses[2:]:
                if exp1 + exp2 + exp3 == 2020:
                    print(
                        f"The three expenses that sum to 2020 are: {exp1}, {exp2}, {exp3}"
                    )
                    return exp1, exp2, exp3
                elif exp1 + exp2 + exp3 > 2020:
                    break


def get_input():
    with open("input.txt") as f:
        return [int(line.strip()) for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    inputs = get_input()
    expense1, expense2 = find_two_expenses_that_sum(inputs)
    multiply_expenses(expense1, expense2)
    print("-" * 20)

    # part 2
    expense1, expense2, expense3 = find_three_expenses_that_sum(inputs)
    multiply_expenses(expense1, expense2, expense3)
