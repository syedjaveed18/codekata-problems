s = input().split()

def reverse(string):
    if len(string) == 1:
        return string
    else:
        new_string = string[0]
        for i in range(1,len(string)-1):
            new_string += string[-(i+1)]
        new_string += string[-1]
        return new_string

new_s = []
for string in s:
    new_s.append(reverse(string))

print(*new_s)
