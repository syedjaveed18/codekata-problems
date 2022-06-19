s = input()
ascii_value = 0
for i in s:
    if i in ['a','e','i','o','u']:
        ascii_value += ord(i)

print(1) if ascii_value%8 == 0 else print(0)
