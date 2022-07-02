n = int(input())
array = list(map(int,input().split()))

indices_diff = array.index(max(array)) - array.index(min(array))

print(indices_diff)
