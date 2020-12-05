def make_seat_map():
    return [[0, 0, 0, 0, 0, 0, 0, 0] for y in range(128)]


def populate_seat_map(boarding_passes, seat_map):
    for boarding_pass in boarding_passes:
        y = [i for i in range(128)]
        x = [i for i in range(8)]
        for index, instruction in enumerate(boarding_pass):
            if instruction == "F":
                y = y[: len(y) // 2]
            elif instruction == "B":
                y = y[len(y) // 2 :]
            elif instruction == "L":
                x = x[: len(x) // 2]
            elif instruction == "R":
                x = x[len(x) // 2 :]

            if index == len(boarding_pass) - 1:
                seat_map[y[0]][x[0]] = 1


def seat_ids(seat_map, return_max=False):
    max_id = 0
    all_ids = {}
    for row, _ in enumerate(seat_map):
        for column, _ in enumerate(seat_map[row]):
            if seat_map[row][column] != 1:
                continue
            current_id = (row * 8) + column
            all_ids[current_id] = None
            if current_id > max_id:
                max_id = current_id
    if return_max:
        return max_id
    return all_ids


def find_seat(seat_map, all_seat_ids):
    for row, _ in enumerate(seat_map):
        for column, _ in enumerate(seat_map[row]):
            if seat_map[row][column] == 1:
                continue
            current_id = (row * 8) + column
            if current_id + 1 in all_seat_ids and current_id - 1 in all_seat_ids:
                return current_id


def get_input():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    inputs = get_input()
    seat_map = make_seat_map()
    populate_seat_map(inputs, seat_map)
    max_id = seat_ids(seat_map, True)
    print(f"Max seat id is {max_id}")

    print("-" * 20)
    # part 2
    all_seat_ids = seat_ids(seat_map)
    santa_seat_id = find_seat(seat_map, all_seat_ids)
    print(f"Santa's seat ID is {santa_seat_id}")
