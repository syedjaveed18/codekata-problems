string = input().split()

output = []

for index,char in enumerate(string):
    if index%2 == 0:
        output.append(char.upper())
    else:
        output.append(char.lower())

print(*output)
