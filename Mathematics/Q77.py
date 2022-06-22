N,K = map(int,input().split())
for n in range(1,min(N,K)+1):
    if N%n == 0 and K%n == 0:
        div = n
print(div)
