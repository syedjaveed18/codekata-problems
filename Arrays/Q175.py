n,k = map(int,input().split())
n_numbers = list(map(int,input().split()))

while True:
    if k in n_numbers:
        print(n_numbers.index(k))
        break
    k -= 1
else:
    print(-1)
