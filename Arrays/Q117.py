n = int(input())

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        return n

prime_factors = []

for i in range(2,n+1):
    if prime(i) and n%i == 0:
        prime_factors.append(i)

print(' '.join([str(j) for j in prime_factors]))
