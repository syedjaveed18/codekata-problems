n,x = map(int,input().split())
array = list(map(int,input().split()))

for a in array:
    array_copy = array.copy()
    array_copy.remove(a)
    flag = False
    for b in array:
        if (a+b) == x:
            print('yes')
            flag = True
            break
    if flag:
        break

if not flag:
    print('no')
