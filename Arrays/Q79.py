x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
x3,y3 = map(float,input().split())

if (y3-y2)*(x2-x1) == (y2-y1)*(x3-x2) :
    print('yes')
else:
    print('no')
