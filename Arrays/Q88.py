n,k = map(int,input().split())

strings = []
for i in range(n):
    s = input()
    strings.append(s)

for i in range(n-k + 1):
    if len(set(strings[i:i+k])) == 1:
        print('yes')
        break
else:
    print('no')
