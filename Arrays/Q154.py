n,k = map(int,input().split())
array = list(map(int,input().split()))

repeated = []
for elem in set(array):
    if array.count(elem) == k:
        repeated.append(elem)

repeated.sort()
print(*repeated) if len(repeated) > 0 else print(-1)
