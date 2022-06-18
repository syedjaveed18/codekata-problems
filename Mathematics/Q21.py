num = int(input())
product = 1
while num > 0:
    rem = num%10
    num = num//10
    product = product*rem
print(product)
