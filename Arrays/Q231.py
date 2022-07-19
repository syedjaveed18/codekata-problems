n = int(input())
N_nunmbers = list(map(int,input().split()))

diff = 0
flag = False
while True:
    for elem1 in N_nunmbers:
        N_nunmbers_copy = N_nunmbers.copy()
        N_nunmbers_copy.remove(elem1)
        for elem2 in N_nunmbers_copy:
            if abs(elem1 + elem2) == diff:
                print(elem1,elem2)
                flag = True
                break
        
        if flag:
            break
    
    if flag:
            break
    diff += 1
