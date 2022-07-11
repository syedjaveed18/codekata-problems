n = int(input())
N_numbers = list(map(int,input().split()))

for i in range(n-2):
    if sum(N_numbers[:i+1]) == sum(N_numbers[i+2:]):
        print('yes')
        break
else:
    print('no')
