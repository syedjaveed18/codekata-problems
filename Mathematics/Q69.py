a,b =  map(int,input().split())
hcf = 1
i = 1
if a==0 or b==0 :
    print("-1")
else:
    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i == 0 :
            hcf = i
            i = i+1
    print(hcf)
