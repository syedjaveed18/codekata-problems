n = int(input())
l = list(map(int,input().split()))
l.sort()
s = ""
for elem in l :
    for i in range(1,elem//4) :
        if elem == (i**3 + (i+1)**3) :
            s += str(elem) + ' '
            break

if len(s) >= 1:
    print(s[:-1])
else:
    print(-1)
