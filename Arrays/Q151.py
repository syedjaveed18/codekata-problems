n,k = map(int,input().split())
array = list(map(int,input().split()))

ascending = array[:k]
ascending.sort()
descending = array[k:]
descending.sort(reverse = True)
new_array = ascending + descending

print(*new_array)
