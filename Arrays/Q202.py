n = int(input())

for i in range(n):
    N,K = map(int,input().split())
    
    array = list(range(1,N+1))
    
    while len(array) >= K:
        array = array[K-1::K]
    
    print(array[0])
