n,k = map(int,input().split())
elements = list(map(int,input().split()))

if k in elements:
    print(elements.count(k)-1)
else:
    print(-1)
