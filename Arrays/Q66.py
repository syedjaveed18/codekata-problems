alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

S = input()
new_string = ""

for i in S:
    j = (alphabets.index(i) + 3)%26
    new_string += alphabets[j]

print(new_string)
