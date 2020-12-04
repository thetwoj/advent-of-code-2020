def how_many_trees(tree_map, x_slope, y_slope):
    x = 0
    y = 0
    trees = 0
    while y <= len(tree_map) - 1:
        if tree_map[y][x % len(tree_map[y])] == "#":
            trees += 1
        y += y_slope
        x += x_slope
    return trees


def get_input():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    input_map = get_input()
    trees = how_many_trees(input_map, 3, 1)
    print(f"Ran into {trees} trees with a 3/1 slope")

    print("-" * 20)
    # part 2
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (x, y)
    trees_encountered = []
    for slope in slopes:
        trees_encountered.append(how_many_trees(input_map, slope[0], slope[1]))

    product = 1
    for tree_count in trees_encountered:
        product *= tree_count

    print(f"Product of trees encountered across all slopes is {product}")
