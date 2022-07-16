n = int(input())

def prime(n):
    if n <= 1:
        return None
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        return n

prime_numbers = []
for i in range(1,n+1):
    if prime(i):
        prime_numbers.append(i)
