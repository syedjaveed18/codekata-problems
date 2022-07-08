n = int(input())
array = list(map(int,input().split()))

prefix_sum = []
for i in range(n):
    prefix_sum.append(sum(array[:i+1])) if sum(array[:i+1])%2 == 0 else prefix_sum.append(array[i])

print(*prefix_sum)
