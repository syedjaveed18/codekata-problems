string = input()
T = int(input())
P = int(input())

new_string = ''
for index,char in enumerate(string):
    if (index + 1)%P == 0:
        if char.islower():
            new_string += char.upper()
        else:
            new_string += char.lower()
    else:
        new_string += char

print(new_string)
