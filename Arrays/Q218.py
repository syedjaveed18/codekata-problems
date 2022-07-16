n = int(input())
array = list(map(int,input().split()))

condition = True
diff = 0
while condition:
    for i in array:
        array_copy = array.copy()
        array_copy.remove(i)
        for j in array_copy:
            if (i + j) == diff:
                print(i,j)
                condition = False
                break
    
        if condition == False:
            break
    
    diff += 1
