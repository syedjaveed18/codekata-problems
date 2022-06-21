P,A = map(int,input().split())
for i in range(1,int(P/2) + 1):
    l = i
    b = int(P/2) - i
    if A == l*b:
        print('yes')
        break
else:
    print('no')
