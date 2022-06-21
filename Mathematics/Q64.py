n = int(input())
for i in range(1,int(n/2)):
    if n == i**2 :
        print('yes')
        break
else:
    print('no')
