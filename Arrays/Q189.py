n = int(input())
n_numbers = list(map(int,input().split()))

result = []
for index,elem in enumerate(n_numbers):
    if index%2 == 0 and elem%2 != 0:
        result.append(elem)
    elif index%2 != 0 and elem%2 == 0:
        result.append(elem)

if len(result) > 0:
    print(*result)
else:
    print(-1)
