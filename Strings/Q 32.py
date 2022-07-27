string  = input()

duplicate = []
for char in set(string):
    if string.count(char) > 1:
        duplicate.append(char)

print(*duplicate) if len(duplicate) > 0 else print(-1)
