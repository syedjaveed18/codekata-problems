k = int(input())

output_array = []
for i in range(k):
    array = list(map(int,input().split()))
    output_array.extend(array)

output_array.sort()

print(*output_array)
