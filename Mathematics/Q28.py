n = int(input())
li = [1]
for i in range(2,n+1):
    li.append(li[-1]+i**3)
print(' '.join([str(elem) for elem in li]))
