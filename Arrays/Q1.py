n = int(input())
li = [1000,1000]
i = 2
if n > 1:
    while i <= n :
        li.append(int(li[-1])+int(li[-2]))
        i+=1
print(sum(li))
