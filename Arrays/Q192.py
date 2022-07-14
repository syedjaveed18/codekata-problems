n,k = map(int,input().split())
array = list(map(int,input().split()))

condition = False
for elem1 in array:
    array_copy = array.copy()
    array_copy.remove(elem1)
    for elem2 in array_copy:
        if elem2 + elem1 == k:
            print('yes')
            condition = True
            break
    if condition:
        break

if not(condition):
    print('no')
