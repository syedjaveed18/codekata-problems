n = int(input())
array = list(map(int,input().split()))

distinct_array = sorted(set(array))
output = []
for i in range(1,n+1):
    for elem in distinct_array:
        if array.count(elem) == i:
            output.append(elem)

print(*output[::-1])
