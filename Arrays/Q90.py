n = int(input())

strings = []
for i in range(n):
    s = input()
    strings.append(s)

for i in range(n-1):
    if len(set(strings[i:i+2])) == 1:
        print('yes')
        break
else:
    print('no')
