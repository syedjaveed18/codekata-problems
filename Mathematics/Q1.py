n = str(int(input()))
sum = 0
for i in n :
    sum = sum + int(i)
if sum%3 == 0:
    print("pure")
else:
    print("not")
