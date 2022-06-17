n = int(input())
sum=0
while n != 0:
    i = n%10
    n = n//10
    sum=sum+i
print(sum)
