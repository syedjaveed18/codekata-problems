s1,s2,k = input().split()

diff = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        diff += 1

if diff == int(k):
    print('yes')
else:
    print('no')
