m,n = map(int,input().split())
diff = abs(m-n)
if diff%2 == 0:
    print('even')
else:
    print('odd')
