n = int(input())
li = [2]
for i in range(2,n+1):
    li.append(li[-1]+2*i)
print(li[n-1])
