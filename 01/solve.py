elves = open("01/input.txt").read().split("\n\n")
elf_dict = {}
for ind, elf in enumerate(elves):
    items = elf.split("\n")
    elf_dict[sum([int(i) for i in items])] = ind

# part 1
print(f"Greatest calories carried by any elf is {max(elf_dict.keys())}")

# part 2
max_three = sorted(elf_dict.keys(), reverse=True)[0:3]
print(f"Sum of max three elves' calories is {sum(max_three)}.")