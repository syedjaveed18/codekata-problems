n = int(input())

def prime(n):
    if n <= 1:
        return None
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        return n

prime_factors = []
for i in range(2,n+1):
    if n%i == 0 and prime(i):
        prime_factors.append(i)

print(*prime_factors)
