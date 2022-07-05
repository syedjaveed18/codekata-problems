n = int(input())
array = list(map(int,input().split()))
result = []

for i in range(n):
    result.append(sum(array[:i+1]) + sum(array[i:]))

print(*result)
