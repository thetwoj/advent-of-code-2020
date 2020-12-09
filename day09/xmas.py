def find_anomaly(inputs, preamble):
    possible_sums = []
    # Generate the initial list of possible sums from the first
    # set of numbers within the size of the preamble
    for index, first in enumerate(inputs[:preamble]):
        for second in inputs[index + 1:preamble]:
            possible_sums.append(first + second)

    for index, x in enumerate(inputs[preamble:]):
        if x not in possible_sums:
            return x
        # To "slide" the window of sums forward strip off the first
        # preamble-1 worth of sums as they all involved the number that
        # is dropping off, then add new sums at the appropriate place
        # in the list so they're at the end of their respective number's
        # section
        #
        # preamble = 4
        # input = [1, 2, 3, 4, 5, 6, 7]
        #
        #  (first int)     1  1  1  2  2  3      2  2  2  3  3  4
        # possible_sums = [3, 4, 5, 5, 6, 7] -> [7, 5, 6, 8, 7, 9]
        #                  ^  ^  ^         2 + 5 ^        ^     ^
        #                  removed                  3 + 5 |     |
        #                                                 4 + 5 |
        possible_sums = possible_sums[preamble-1:]  # remove preamble - 1 from the front
        for index2, i in enumerate(inputs[index+1:index+preamble]):
            offset = sum([y for y in range(index2+1)])
            possible_sums.insert((preamble*index2)-offset, i + x)


def find_contiguous_sum(inputs, target):
    start = 0
    end = 1
    total = inputs[start] + inputs[end]
    while total != target:
        if total > target:
            start += 1
        elif total < target:
            end += 1
        total = sum([x for x in inputs[start:end]])

    sorted_range = sorted(inputs[start:end])
    return sorted_range[0] + sorted_range[-1]


def get_input():
    with open("input.txt") as f:
        return [int(line.strip()) for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    preamble = 25
    inputs = get_input()
    anomaly = find_anomaly(inputs, preamble)
    print(f"{anomaly} was not a sum of previous {preamble} numbers")

    print("-" * 20)
    # part 2
    total = find_contiguous_sum(inputs, anomaly)
    print(f"{total} is the sum of the smallest and largest in the contiguous range that sum to {anomaly}")