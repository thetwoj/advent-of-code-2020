def count_gaps(adapters):
    one_gap = 0
    three_gap = 1
    previous = 0
    for adapter in adapters:
        if adapter - previous == 1:
            one_gap += 1
        if adapter - previous == 3:
            three_gap += 1
        previous = adapter
    return one_gap, three_gap


def get_input():
    with open("input.txt") as f:
        return [int(line.strip()) for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    preamble = 25
    adapters = get_input()
    adapters.sort()
    one_gap, three_gap = count_gaps(adapters)
    product = one_gap * three_gap
    print(f"{product} is the product of 1 jolt gaps and 3 jolt gaps")

    print("-" * 20)
    # part 2
