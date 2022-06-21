n = int(input())
odd_factors = []
for i in range(1,n+1):
    if n%i == 0 and i%2 == 1:
        odd_factors.append(i)
print(' '.join([str(elem) for elem in odd_factors]))
