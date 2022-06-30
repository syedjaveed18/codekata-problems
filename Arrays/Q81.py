n = int(input())
array = list(map(int,input().split()))

sum = 0
for i in range(n-1):
    sum += array[i] + array[i+1]

print(sum)
