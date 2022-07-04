n = int(input())
array = list(map(int,input().split()))
array.sort()

length_array = []
count = 0
for i in range(len(array)-1):
    if (array[i+1] - array[i]) == 1:
        count += 1
    else:
        count = 0
    length_array.append(count)

print(max(length_array)+1)
