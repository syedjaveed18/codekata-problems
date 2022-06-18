a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())
a4,b4 = map(int,input().split())

d1 = (a1-a3)**2 + (b1-b3)**2
d2 = (a4-a2)**2 + (b4-b2)**2

if d1 == d2:
    print('yes')
else:
    print('no')
