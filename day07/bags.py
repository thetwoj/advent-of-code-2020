def count_bags_within(rule, rules, count):
    if not rules[rule]:
        return 0

    for nested_bag in rules[rule]:
        count += rules[rule][nested_bag] + (
            rules[rule][nested_bag] * count_bags_within(nested_bag, rules, 0)
        )

    return count


def find_bag_within(rule, rules, desired_bag):
    if rule == desired_bag:
        return True

    for nested_bag in rules[rule]:
        if find_bag_within(nested_bag, rules, desired_bag):
            return True


def find_shiny_gold(rules):
    contains_shiny_gold = 0
    for rule in rules:
        if rule == "shiny gold":
            continue
        if find_bag_within(rule, rules, "shiny gold"):
            contains_shiny_gold += 1
    return contains_shiny_gold


def extract_rules(inputs):
    rules = {}
    for line in inputs:
        words = line.split(" ")
        origin_bag = " ".join([words[0], words[1]])
        rules[origin_bag] = {}
        for index, word in enumerate(words):
            if word.isnumeric():
                count = word
                nested_bag = " ".join([words[index + 1], words[index + 2]])
                rules[origin_bag][nested_bag] = int(count)
    return rules


def get_input():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    inputs = get_input()
    bag_rules = extract_rules(inputs)
    contain_shiny_gold_count = find_shiny_gold(bag_rules)
    print(f"{contain_shiny_gold_count} bags contain shiny gold bags")

    print("-" * 20)
    # part 2
    bag_count = count_bags_within("shiny gold", bag_rules, 0)
    print(f"shiny gold bag contains {bag_count} other bags")
