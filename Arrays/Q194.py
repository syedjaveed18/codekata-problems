n,k = map(int,input().split())
n_integers = list(map(int,input().split()))

while True:
    if k in n_integers:
        n_integers.remove(k)
    else:
        break
if len(n_integers) > 0:
    print(*n_integers)
else:
    print('empty')
