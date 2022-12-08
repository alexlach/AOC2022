input_lines = open("08/input.txt").read().split("\n")
tree_arr = []
for line in input_lines:
    tree_arr.append([int(cell) for cell in list(line)])

visible_trees = 0
for y in range(len(tree_arr)):
    for x in range(len(tree_arr[0])):
        blocked_sides = 0
        tree_height = tree_arr[y][x]
        for y_check in range(0, y):
            if tree_arr[y_check][x] >= tree_height:
                blocked_sides += 1
                break

        for y_check in range(y + 1, len(tree_arr)):
            if tree_arr[y_check][x] >= tree_height:
                blocked_sides += 1
                break

        for x_check in range(0, x):
            if tree_arr[y][x_check] >= tree_height:
                blocked_sides += 1
                break

        for x_check in range(x + 1, len(tree_arr[0])):
            if tree_arr[y][x_check] >= tree_height:
                blocked_sides += 1
                break

        if blocked_sides < 4:
            visible_trees += 1

print(visible_trees)

# find scenic scores
scenic_scores = []
for y in range(len(tree_arr)):
    for x in range(len(tree_arr[0])):
        tree_height = tree_arr[y][x]
        previous_tree = -1
        view_north = 0
        for y_check in reversed(range(0, y)):
            if previous_tree < tree_height:
                view_north += 1
                previous_tree = tree_arr[y_check][x]
            else:
                break

        previous_tree = -1
        view_south = 0
        for y_check in range(y + 1, len(tree_arr)):
            if previous_tree < tree_height:
                view_south += 1
                previous_tree = tree_arr[y_check][x]
            else:
                break

        previous_tree = -1
        view_west = 0
        for x_check in reversed(range(0, x)):
            if previous_tree < tree_height:
                view_west += 1
                previous_tree = tree_arr[y][x_check]
            else:
                break

        previous_tree = -1
        view_east = 0
        for x_check in range(x + 1, len(tree_arr[0])):
            if previous_tree < tree_height:
                view_east += 1
                previous_tree = tree_arr[y][x_check]
            else:
                break

        scenic_scores.append(view_east * view_north * view_south * view_west)

print(max(scenic_scores))
