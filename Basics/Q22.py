a,b = map(int,input().split())
j=0
for n in range(a,b+1) :
    if n>1 :
        for i in range(2,n) :
            if (n%i) == 0 :
                break
        else:
            j+=1
print(j)
