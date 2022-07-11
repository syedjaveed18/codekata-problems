n = int(input())

even_factors = []
for i in range(2,n+1,2):
    if n%i == 0:
        even_factors.append(i)

if len(even_factors) > 0:
    print(' '.join([str(i) for i in even_factors]))
else:
    print(-1)
