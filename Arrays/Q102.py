n = int(input())
array = input().split()

beautiful_indices = 0
for i in range(0,n-1):
    if array.count(array[i]) == array[i+1]:
        beautiful_indices += 1

print(beautiful_indices)
