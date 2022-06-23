m,n = map(int,input().split())

l1 = []
for i in range(m):
    l2 = list(map(int,input().split()))
    l1.extend(l2)

l1.sort()
x =0
for j in range(m):
    print(" ".join([str(elem) for elem in l1[x:x+3]]))
    x = x+3
