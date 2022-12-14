commands = open("10/input.txt").read().split("\n")

cmd_archive = []
for command in commands:
    if command != "noop":
        cmd_archive.append(int(command.split(" ")[1]))
    cmd_archive.append(0)

cum_cmds = [1 + sum(cmd_archive[0:i]) for i in range(len(cmd_archive))]
samples = [20, 60, 100, 140, 180, 220]
print(sum([i * cum_cmds[i - 2] for i in samples]))

crt = ["#" if abs((i + 1) % 40 - cum_cmds[i]) <= 1 else " " for i in range(len(cum_cmds))]
print("".join(crt))
