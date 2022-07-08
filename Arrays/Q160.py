days = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if sum(A) == sum(B):
    print('yes')
else:
    for i in range(days):
        A_copy = A.copy()
        B_copy = B.copy()
        A_copy[i] = B[i]
        B_copy[i] = A[i]
        if sum(A_copy) == sum(B_copy):
            print('yes')
            break
    else:
        print('no')
