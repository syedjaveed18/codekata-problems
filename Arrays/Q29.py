n = input()
array = list(map(int,input().split()))
sum = 0
for num in array:
    if num < 0:
        sum = sum + num
print(sum)
