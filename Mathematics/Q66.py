n,k = map(int,input().split())
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

print(factorial(n)/factorial(n-k))
