n = int(input())
array = list(map(int,input().split()))

N = 1

while True:
    count = 0
    for elem in array:
        if N%elem != 0:
            N += 1
            break
        else:
            count += 1

    if count == n:
        print(N)
        break
