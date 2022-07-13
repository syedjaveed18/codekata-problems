n,m = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

if A.intersection(B) == B:
    print('yes')
else:
    print('no')
