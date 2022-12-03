sacks = open("03/input.txt").read().split("\n")


def get_prio(letter):
    """get ascii index of character and adjust it to our scoring system"""
    if letter.lower() == letter:
        return ord(letter) - 96
    else:
        return ord(letter) - 38


# part 1
sum = 0
for sack in sacks:
    first = sack[: (len(sack) // 2)]
    second = sack[(len(sack) // 2) :]
    sum += get_prio(list(set(first) & set(second))[0])
print(sum)

# part 2
sum = 0
for group in range(0, len(sacks), 3):
    badge = list(set(sacks[group]) & set(sacks[group + 1]) & set(sacks[group + 2]))[0]
    sum += get_prio(badge)
print(sum)