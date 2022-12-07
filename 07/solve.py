input_lines = open("07/input.txt").read().split("\n")

# Initialize the dictionary representing the file system
file_system = {}
file_system["/"] = {}
current_dir = file_system["/"]
parent_dirs = []

# Parse the file system
for line in input_lines:
    if line[0] == "$":  # If this is a command line, process it
        words = line.split()
        cmd = words[1]
        args = words[2:]

        if cmd == "cd":
            if args[0] == "/":
                current_dir = file_system["/"]
            elif args[0] == "..":
                current_dir = parent_dirs.pop()
            else:
                parent_dirs.append(current_dir)
                current_dir = current_dir[args[0]]
        elif cmd == "ls":
            for entry in current_dir:
                if entry == "..":
                    continue
                entry_type = "dir" if isinstance(current_dir[entry], dict) else "file"
                print(f"{entry_type} {entry}")
    else:
        words = line.split()
        entry_type = words[0]
        entry_name = words[1]

        if entry_type == "dir":
            current_dir[entry_name] = {}
        else:
            current_dir[entry_name] = int(entry_type)


def add_integer_values(d, path_hist=""):
    sum = 0
    for key, value in d.items():
        if isinstance(value, dict):
            # Recursively add the integer values in the nested dictionary
            nested_sum = add_integer_values(value, path_hist + "/" + key)
            directory_totals[path_hist + "/" + key] = nested_sum
            sum += nested_sum
        else:
            if isinstance(value, int):
                sum += value
    return sum


directory_totals = {}
add_integer_values(file_system)
print(sum([d for d in directory_totals.values() if d <= 100000]))
space_to_release = 30000000 - (70000000 - max(directory_totals.values()))
print(min(size for size in directory_totals.values() if size >= space_to_release))