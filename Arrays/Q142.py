n = int(input())
array = list(map(int,input().split()))

div = []
for elem1 in array:
    for elem2 in array:
        if elem2%elem1 != 0:
            break
    else:
        div.append(elem1)

print(max(div))
