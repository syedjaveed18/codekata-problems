N,K = map(int,input().split())
for i in range(10):
    if N == K**i:
        print('yes')
        break
else:
    print('no')
