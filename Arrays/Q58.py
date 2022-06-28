n,k = map(int,input().split())
elements = list(map(int,input().split()))
elem = elements.copy()

for i in elements:
    if i >= k:
        elem.remove(i)

elem.sort()

if len(elem) > 0:
    print(" ".join([str(j) for j in elem]))
else:
    print(-1)
