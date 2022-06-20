n = int(input())

def prime(n):
    if n == 1:
        return None
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        return n
i = 2
prime_factors = []
while n > 1:
    if prime(i) :
        while n%i == 0:
            prime_factors.append(i)
            n = n//i
    i += 1

prime_factors_count = []
for i in set(prime_factors):
    prime_factors_count.append(prime_factors.count(i))

print(sum(prime_factors_count))
