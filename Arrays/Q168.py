N = int(input())

def sum_of_digits(i):
    sum_digits = 0
    while i > 0:
        rem = i%10
        i = i//10
        sum_digits = sum_digits + rem
    return sum_digits
    
if str(sum_of_digits(N)) == str(sum_of_digits(N))[::-1]:
    print('yes')
else:
    print('no')
