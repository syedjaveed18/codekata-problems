n = int(input())
array = list(map(int,input().split()))
even_pos = [elem for elem in array[::2]]
even_pos.sort()

i = 0
for elem in even_pos:
    array[i] = elem
    i += 2

print(' '.join([str(n) for n in array]))
