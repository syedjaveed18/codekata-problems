n = int(input())
array = list(map(int,input().split()))

lucky_number = 0
for i in range(1,n+1):
    if n*i in array:
        lucky_number += 1

print(lucky_number)
