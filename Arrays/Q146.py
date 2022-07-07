n = int(input())
odd_digits = [int(i) for i in str(n) if int(i)%2 != 0]
if sum(odd_digits)%2 == 0:
    print('E')
else:
    print('O')
