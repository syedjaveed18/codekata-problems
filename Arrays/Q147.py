n,k = map(int,input().split())
array = list(map(int,input().split()))

array.sort()
new_list = []

for i in array:
    if array.count(i) < 2:
        new_list.append(i)

print(*new_list)
