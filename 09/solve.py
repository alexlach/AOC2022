input_lines = open("09/input.txt").read().split("\n")


def move_tail(head, tail):
    new_x = tail[0]
    new_y = tail[1]
    distance_x = tail[0] - head[0]
    distance_y = tail[1] - head[1]
    if abs(distance_x) <= 1 and abs(distance_y) <= 1:
        return tail  # if adjacent, no need for the tail to move
    elif abs(distance_x) > 0 and abs(distance_y) > 0:
        if distance_x >= 1:
            new_x = tail[0] - 1  # move tail left
        elif distance_x <= -1:
            new_x = tail[0] + 1  # move tail right
        if distance_y >= 1:
            new_y = tail[1] - 1  # move tail down
        elif distance_y <= -1:
            new_y = tail[1] + 1  # move tail up
    elif distance_x > 1:
        new_x = tail[0] - 1  # move tail left
    elif distance_x < -1:
        new_x = tail[0] + 1  # move tail right
    elif distance_y > 1:
        new_y = tail[1] - 1  # move tail down
    elif distance_y < -1:
        new_y = tail[1] + 1  # move tail up

    return [new_x, new_y]


dir_dict = {"L": -1, "R": 1, "D": -1, "U": 1}
knot_locs = [[0, 0] for _ in range(10)]
tail_location_archive = [[] for _ in range(10)]

for line in input_lines:
    direction, distance = line.split(" ")
    for i in range(int(distance)):
        knot_locs[0][0] += dir_dict[direction] if direction in ("L", "R") else 0
        knot_locs[0][1] += dir_dict[direction] if direction in ("U", "D") else 0
        for knot_index in range(len(knot_locs) - 1):
            knot_locs[knot_index + 1] = move_tail(knot_locs[knot_index], knot_locs[knot_index + 1])
            tail_location_archive[knot_index].append(tuple(knot_locs[knot_index + 1]))
print(len(set(tail_location_archive[0])))  # part 1
print(len(set(tail_location_archive[8])))  # part 2
