n = int(input())
array = input().split()
set_array = set(array)

length = []
for i in set_array:
    count = 0
    pos = array.index(i)
    for elem in array[pos:]:
        if elem == i:
            count += 1
        else:
            break
    length.append(count)

if max(length) >= 2:
    print(max(length))
else:
    print(-1)
