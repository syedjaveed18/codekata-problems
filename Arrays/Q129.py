s = input()

char_repeated = []
for i in s:
    char_repeated.append(s.count(i))

if max(char_repeated) > 1:
    print(max(char_repeated))
else:
    print(0)
