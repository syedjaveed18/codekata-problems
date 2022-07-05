t = int(input())

for i in range(t):
    n = int(input())
    array = list(set(list(map(int,input().split()))))
    k = int(input())
    array.sort()
    print(array[k-1])
