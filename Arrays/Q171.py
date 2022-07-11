n = int(input())
m = n+1
if n < int(''.join(sorted(str(n),reverse=True))):
    while m <= int(''.join(sorted(str(n),reverse=True))):
        if sorted(str(n)) == sorted(str(m)):
            print(m)
            break
        m+=1
else:
    print('impossible')
