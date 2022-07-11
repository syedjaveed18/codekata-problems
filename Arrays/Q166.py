n = int(input())
array = list(map(int,input().split()))

if n%2 == 0:
    index = n//2
else:
    index = int(n/2)

ascending = array[:index]
descending = array[index:]
ascending.sort()
descending.sort(reverse = True)

output = ascending + descending
print(*output)
