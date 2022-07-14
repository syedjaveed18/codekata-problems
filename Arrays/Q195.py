s = input().split()

new_string = [word[::-1] for word in s]
print(*new_string)
