n = input()
unique = set(n)
frequency = []

for i in unique:
    frequency.append(n.count(i))

if len(set(frequency)) > 1:
    print(0)
else:
    print(1)
