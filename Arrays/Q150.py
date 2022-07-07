n = int(input())
array = list(map(int,input().split()))
array.sort()

if array == list(range(1,n+1)):
    print('yes')
else:
    print('no')
