from itertools import permutations
 
s = input()
p = permutations(s)
 
# Create a dictionary
d = []
for i in list(p):
 
    # Print only if not in dictionary
    if (i not in d):
        d.append(i)
        print(''.join(i))
