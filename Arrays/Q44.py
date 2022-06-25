n = int(input())
books_in_shelf = list(map(int,input().split()))
m = int(input())
books_to_placed = list(map(int,input().split()))
pos = []
for i in books_to_placed:
    x = 0
    for j in books_in_shelf:
        if i < j:
            x += 1
    pos.append(x+1)

print(" ".join([str(x) for x in pos]))
