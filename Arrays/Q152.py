n = int(input())
array = list(map(int,input().split()))

lesser = [i for i in array if i < n]
lesser.sort(reverse = True)

print(*lesser) if len(lesser) > 0 else print(-1)
