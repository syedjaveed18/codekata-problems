n = int(input())
factors = 0
for i in range(1,n+1) :
    if n%i == 0 :
        factors+=1
    

if factors>=3:
    print("yes")
else:
    print("no")
