n = int(input())
array = input().split()

new_array = []
while len(array) > 0:
    if len(array)%2 == 0:
        m = len(array)//2
    else:
        m = len(array)//2 + 1
    new_array.append(array[m-1])
    array.remove(array[m-1])

print(*new_array)
