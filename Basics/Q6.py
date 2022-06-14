n = int(input())
j = 0
d = 1
for i in range(1,n+1) :
    if n%i == 0 :
        j+=1
    

if j>=3:
    print("yes")
else:
    print("no")
