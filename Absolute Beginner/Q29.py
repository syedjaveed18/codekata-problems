import math
a,b,c = map(int,input().split())
r = -b/(2*a)
i = math.sqrt((b*b)-(4*a*c))/(2*a)
X = r + i
Y = r - i
print(f'{X:.2f}')
print(f'{Y:.2f}')
