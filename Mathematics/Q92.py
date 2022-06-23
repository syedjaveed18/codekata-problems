n = int(input())
for i in range(1,n//10):
    if n == 2**i:
        print('yes')
        break
else:
    print('no')
