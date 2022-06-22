n = int(input())
binary = ''
while n > 0:
    rem = n%2
    n = n//2
    binary = binary + str(rem)

p = 0
for i in binary:
    if i == '1':
        break
    p+=1
print(p+1)
