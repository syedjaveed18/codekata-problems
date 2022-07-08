n = int(input())

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        return n

count = 0

for i in range(2,n+1):
    if prime(i):
        for j in range(2,n+1):
            if prime(j):
                if prime(i)*prime(j) == n and prime(i) >= prime(j):
                    print(prime(i),prime(j))
                    count+=1

if count == 0:
    print(-1)
