n,d = map(int,input().split())
array = input().split()

if d > 4:
    i = d//4
else:
    i = d

new_array = array[i:] + array[:i]

print(*new_array)
