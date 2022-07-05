n = int(input())
array = list(map(int,input().split()))

sorted_array = sorted(array)

original_indices = []
for elem in sorted_array:
    original_indices.append(array.index(elem) + 1)

print(*original_indices)
