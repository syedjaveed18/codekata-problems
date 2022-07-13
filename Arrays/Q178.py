n,k = map(int,input().split())

array = set(map(int,input().split()))
for i in range(n-1):
    array1 = set(map(int,input().split()))
    array = array.intersection(array1)

if len(array) > 0:
    print(*array)
else:
    print(-1)
