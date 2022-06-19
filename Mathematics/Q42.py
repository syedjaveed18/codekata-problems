n = int(input())
array = list(map(int,input().split()))
if sum(array[:3]) == sum(array[-3:]):
    print(1)
else:
    print(0)
