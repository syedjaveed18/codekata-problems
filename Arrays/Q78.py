n = int(input())
a = set(map(int,input().split()))
b = set(map(int,input().split()))
c = a.intersection(b)
d = list(c)
d.sort()
if len(d) == 0:
    print(-1)
else:
    print(" ".join([str(i) for i in d]))
