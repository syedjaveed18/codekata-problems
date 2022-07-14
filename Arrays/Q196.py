n = int(input())
N_numbers = list(map(int,input().split()))

pairs = 0
for a in range(n):
    for b in range(n):
        if a < b and N_numbers[a] < N_numbers[b]:
            pairs += 1

print(pairs)
