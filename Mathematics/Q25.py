n = int(input())
inp = list(map(int,input().split()))
k = int(input())
s = ''
for elem in inp:
    if elem%k == 0:
        s = s + '1' + ' '
    else:
        s = s + '0' + ' '
print(s[:-1])
