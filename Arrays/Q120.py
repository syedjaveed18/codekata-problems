m,n = map(int,input().split())
for i in range(1,100000):
    if i%m == 0 and i%n == 0:
        break

print(i)
