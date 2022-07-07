n = int(input())
array = list(map(int,input().split()))

difference_array = []
for elem1 in array:
    array_copy =  array.copy()
    array_copy.remove(elem1)
    for elem2 in array_copy:
        difference_array.append(abs(elem2-elem1))

print(min(difference_array))
