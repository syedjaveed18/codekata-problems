n = int(input())
array =  list(map(int,input().split()))

check = True
for i in range(1,n,2):
    if array[i-1] < array[i] > array[i+1]:
        pass
    else:
        print('no')
        check = False
        break

if check:
    print('yes')
