n = int(input())
array = list(map(int,input().split()))

count = 0
for i in array:
    for j in array:
        if i < j:
            count += 1

print(count)
