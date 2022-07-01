N,K = map(int,input().split())
array = input().split()
if K >= len(array):
    K = K - len(array)
new_array = array[-K:] + array[:len(array)-K]
print(' '.join(new_array))
