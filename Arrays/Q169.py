n = int(input())
n_numbers = list(map(int,input().split()))

repeated = []
for elem in set(n_numbers):
    if n_numbers.count(elem) > 1:
        repeated.append(elem)

repeated.sort()

if len(repeated) > 0:
    print(*repeated)
else:
    print('unique')
