N = int(input())
n = N
sum_of_digits = 0
product_of_digits = 1
while n != 0 :
    i = n%10
    n = n//10
    sum_of_digits = sum_of_digits + i
    product_of_digits = product_of_digits*i
if (sum_of_digits + product_of_digits) == N :
    print("Great")
else:
    print("no")
