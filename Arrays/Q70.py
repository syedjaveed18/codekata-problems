s = input()
swap_string = ''
i = 0
while i < len(s):
    swap_string += s[i+1]
    swap_string += s[i]
    i += 2

print(swap_string)
