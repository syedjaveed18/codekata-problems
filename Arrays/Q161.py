n = int(input())
array = list(map(int,input().split()))
array.sort()

for elem1 in array:
    Flag = False
    array_copy = array.copy()
    array_copy.remove(elem1)
    for elem2 in array_copy:
        if elem2+elem1 in array:
            print(elem1+elem2)
            Flag = True
            break
    if Flag:
        break
