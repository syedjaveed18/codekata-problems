n = int(input())
books_in_shelf = list(map(int,input().split()))
m = int(input())
books_to_placed = list(map(int,input().split()))

position_newbooks = []

for newbook in books_to_placed:
    pos = 1
    for book in books_in_shelf:
        if newbook < book:
            pos += 1
    
    position_newbooks.append(pos)

print(*position_newbooks)
