n = int(input())
for i in range(1,n+1):
    if n%i == 0 and (n/i)%2 == 1:
        break
print(i)
