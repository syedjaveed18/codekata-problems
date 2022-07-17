n,k = map(int,input().split())
array = input().split()

if k < n:
    pass
else:
    k = k%n

rotated_array = array[k:] + array[:k]

print(*rotated_array)
