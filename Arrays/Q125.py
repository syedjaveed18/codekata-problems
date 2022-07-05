n = int(input())
array = list(map(int,input().split()))

distinct_elements = []
for i in range(n):
    for j in range(n):
        if (i < j) and (array[i] < array[j]):
            distinct_elements.append(str(array[i])+str(array[j]))

if len(set(distinct_elements)) > 0:
    print(len(set(distinct_elements)))
else:
    print(-1)
