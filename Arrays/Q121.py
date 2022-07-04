import math
L,R = map(int,input().split())
count = 0
for i in range(L,R+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        count+=1

if count > 0:
    print(count)
else:
    print(-1)
