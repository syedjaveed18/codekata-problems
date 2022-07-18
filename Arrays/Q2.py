n = int(input())
array = list(map(int,input().split()))

total_air = []
for i in range(n):
    a = max(array[:i+1])
    b = max(array[i:])
    air_stored = min(a,b) - array[i]
    total_air.append(air_stored)

print(sum(total_air))
