n = int(input())
array = list(map(int,input().split()))

Flag = False
for i in array:
    if i%2 == 0:
        Flag = True
        break

if Flag:
    print('even')
else:
    print('odd')
