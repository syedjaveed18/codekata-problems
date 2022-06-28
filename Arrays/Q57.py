n = int(input())
integers = list(map(int,input().split()))
sum_consecutive = []
for i in range(n-1):
    sum_consecutive.append(integers[i]+integers[i+1])

print(max(sum_consecutive))
