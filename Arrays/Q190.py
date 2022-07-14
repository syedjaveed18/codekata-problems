n = int(input())
array = list(map(int,input().split()))

for elem in array:
    if array.count(elem) == 1:
        print(elem)
        break
