n = int(input())
array = list(map(int,input().split()))

prefix_sum = []
for i in range(n):
    prefix_sum.append(sum(array[:i+1]))

print(*prefix_sum)
