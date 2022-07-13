n = int(input())
n_numbers = list(map(int,input().split()))

num_equals_index = []
for i in range(n):
    if i == n_numbers[i]:
        num_equals_index.append(n_numbers[i])

if len(num_equals_index) > 0:
    num_equals_index.sort()
    print(*num_equals_index)
else:
    print(-1)
