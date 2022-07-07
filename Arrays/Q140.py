n = int(input())
array = list(map(int,input().split()))

count_array = []
for elem in array:
    count_array.append(array.count(elem))

print(array[count_array.index(min(count_array))])
