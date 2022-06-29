n = int(input())
array = list(map(int,input().split()))
unique_elem = list(set(array))
count_list = []

for i in unique_elem:
    count_list.append(array.count(i))
    
values = []
for i in unique_elem:
    if array.count(i) == min(count_list) :
        values.append(i)

values.sort(reverse = True)

print(" ".join([str(i) for i in values]))
