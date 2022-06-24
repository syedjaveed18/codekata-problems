n,R = map(int,input().split())
classm = list(map(int,input().split()))

if R in classm:
    print(classm.index(R))
else:
    print(-1)
