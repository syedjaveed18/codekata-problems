n = input()
array = list(map(int,input().split()))
print(array.index(max(array)) - array.index(min(array)))
