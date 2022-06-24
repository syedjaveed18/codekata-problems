n = int(input())
array = list(map(int,input().split()))
sorted_array = sorted(array, reverse = True)

index_pos = []
for i in sorted_array:
    index_pos.append(array.index(i))

print(" ".join([str(i) for i in index_pos]))
