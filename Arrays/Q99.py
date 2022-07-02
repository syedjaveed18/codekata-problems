n = int(input())
array = list(map(int,input().split()))
removed_array = []
for i in array:
    if i in removed_array:
        pass
    else:
        removed_array.append(i)

print(*removed_array)
