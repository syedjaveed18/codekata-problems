n = int(input())
array = list(map(int,input().split()))

new_array = []
for index,elem in enumerate(array):
    if index <= n - 2 :
        for elem2 in array[index + 1:]:
            if elem2 < elem:
                new_array.append(elem2)
                break
        else:
            new_array.append(-1)

new_array.append(-1)

print(" ".join([str(n) for n in new_array]))
