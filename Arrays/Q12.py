n = int(input())
array = list(map(int,input().split()))

common_id = ""
for id in array:
    if array.count(id) > 1:
        common_id = common_id + str(id) + " "
        array.remove(id)

if len(common_id) > 0:
    print(common_id[:-1])
else:
    print(-1)
