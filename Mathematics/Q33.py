n = input()
o = ''
count = 0
for num in n:
    if int(num)%2 != 0:
        o = o + num + ' '
        count+=1
if count > 0:
    print(o[:-1])
else:
    print(-1)
