n = int(input())
for i in range(1,n):
    if 2**i > n:
        break
print(2**i)
