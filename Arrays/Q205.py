n = int(input())

for j in range(1,100000000000):
    i = j
    sum_digits = 0
    while i > 0:
        rem = i%10
        i = i//10
        sum_digits = sum_digits + rem
    if sum_digits == n:
        print(j)
        break
