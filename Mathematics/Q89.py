num = int(input())

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

def sum_factorial(n):
    sum = 0
    while n > 0:
        rem = n%10
        n = n//10
        sum = sum + factorial(rem)
    return sum

for m in range(1,num+1):
    if sum_factorial(m) == num:
        print(m)
        break
else:
    print(-1)
