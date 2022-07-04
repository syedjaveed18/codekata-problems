n = int(input())
array = list(map(int,input().split()))

for elem in array:
    array_copy = array.copy()
    array_copy.remove(elem)
    if elem in array_copy:
        continue
    else:
        print(elem)
        break
