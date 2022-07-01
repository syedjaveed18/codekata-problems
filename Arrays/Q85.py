n,k = map(int,input().split())
array_numbers = list(map(int,input().split()))

if k in array_numbers:
    print("yes",array_numbers.count(k))
else:
    print('no')
