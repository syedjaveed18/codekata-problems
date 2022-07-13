n = int(input())
N_numbers = list(map(int,input().split()))

smallest = [min(N_numbers[:i]) for i in range(1,n+1)]

print(*smallest)
