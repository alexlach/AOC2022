pairs = open("04/input.txt").read().split("\n")

clean_coords = []
for pair in pairs:
    elf1, elf2 = pair.split(",")
    a1, b1 = elf1.split("-")
    a2, b2 = elf2.split("-")
    clean_coords.append((int(a1), int(b1), int(a2), int(b2)))

# Count pairs where one range fully contains the other
overlaps = 0
for (a1, b1, a2, b2) in clean_coords:
    if (a1 <= a2 and b1 >= b2) or (a1 >= a2 and b1 <= b2):
        overlaps += 1

print(overlaps)

overlaps = 0
for (a1, b1, a2, b2) in clean_coords:
    if (a1 <= a2 <= b1) or (a1 <= b2 <= b1) or (a2 <= a1 <= b2) or (a2 <= b1 <= b2):
        overlaps += 1
print(overlaps)