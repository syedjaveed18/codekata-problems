n = int(input())
m = n
no_digits = 0
while m > 0:
    m = m//10
    no_digits+=1
    
sum = 0
while n > 0:
    rem = n%10
    n = n//10
    sum = sum + rem**no_digits
    
print(sum)
