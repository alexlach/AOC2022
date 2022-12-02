rounds = open("02/input.txt").read().split("\n")

# part 1
points = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
print(f"My score is {sum([points[round] for round in rounds])}.")

# part 2
points = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}
scores = [points[round] for round in rounds]
print(f"My score is {sum([points[round] for round in rounds])}.")
