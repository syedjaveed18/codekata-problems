n = input()
sum = 0
for x,y in enumerate(n):
    sum = sum + int(y)**x
    
print(sum)
