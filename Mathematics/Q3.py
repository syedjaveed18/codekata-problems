m,n = map(int,input().split())
count = 0
for i in range(2,min(m,n)+1):
    if m%i == 0 and n%i == 0:
        count+=1
if count > 0:
    print(0)
else:
    print(1)
