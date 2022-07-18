n = int(input())
array = list(map(int,input().split()))
array.sort()

frequency = 1
sorted_array = []
while frequency  <= n:
    for num in set(array):
        if array.count(num) == frequency:
            sorted_array.append(num)
    frequency += 1

print(*sorted_array)
