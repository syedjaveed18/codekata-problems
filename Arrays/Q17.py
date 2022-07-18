n = int(input())
array = list(map(int,input().split()))

for i in range(n):
   array[i]=array[i]+(array[array[i]]%n)*n

for i in range(n):
   array[i]=int(array[i]/n)

print(*array)
