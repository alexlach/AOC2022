def find_consecutive_chars(s, n):
    for i in range(len(s) - n):
        if len(set(s[i : (i + n)])) == n:
            return i + n


s = open("06/input.txt").read()
print(find_consecutive_chars(s, 4))
print(find_consecutive_chars(s, 14))
