n,k = input().split()

Flag = True
for i in range(int(k)+1):
    if i in sorted(n):
        pass
    else:
        Flag = False
        print('no')
        break

if Flag:
    print('yes')
