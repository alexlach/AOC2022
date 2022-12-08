import re
import copy

start, moves = open("05/input.txt").read().split("\n\n")

# parse initial setup of the stacks
stack_count = int(start[-2])
initial_stacks = start.split("\n")
stacks = [[] for _ in range(stack_count)]
for row in initial_stacks[:-1]:
    for i in range(stack_count):
        str_index = 1 + i * 4
        stack_item = row[str_index]
        if stack_item != " ":
            stacks[i].append(stack_item)
stacks = [stack[::-1] for stack in stacks]
stacks_original = copy.deepcopy(stacks)

# part 1
for move in moves.split("\n"):
    _, quantity, _, start, _, end = move.split(" ")
    for i in range(int(quantity)):
        moved_item = stacks[int(start) - 1].pop()
        stacks[int(end) - 1].append(moved_item)
print(f"The message is {''.join([s.pop() for s in stacks])}.")


# part 2
stacks = stacks_original
for move in moves.split("\n"):
    _, quantity, _, start, _, end = move.split(" ")
    items_to_add = []
    for i in range(int(quantity)):
        moved_item = stacks[int(start) - 1].pop()
        items_to_add.append(moved_item)
    for item in items_to_add[::-1]:
        stacks[int(end) - 1].append(item)
print(f"The message is {''.join([s.pop() for s in stacks])}.")
