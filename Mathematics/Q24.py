s = str(input())
n = "0123456789"
sum = 0
for i in s :
    if i in n :
        sum = sum+int(i)
        
print(sum)
