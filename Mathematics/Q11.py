n = int(input())
count = 0
for i in range(1,n+1):
    rev = 0
    num = i
    while num > 0:
        rem = num%10
        num = num//10
        rev = rev*10 + rem
    if i == rev:
        count+=1
print(count)
