n = int(input())
 
arrays = []
for i in range(n):
    m = int(input())
    array = list(map(int,input().split()))
    arrays.append(array)

for array in arrays:
    if arrays.count(array) > 1:
        print('YES')
        break
else:
    print('NO')
