import math
r = float(input())
if r<0:
    print("Error")
else:
    c = 2*(math.pi)*r
    print(format(c,'.2f'))
