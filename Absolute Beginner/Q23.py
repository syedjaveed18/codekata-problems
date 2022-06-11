n = int(input())
y = str(n)
l = sorted(y)
z = ''.join(l)
y = ""
for i in z :
    if int(i)%2 == 0 :
        y = y + i + " "
print(y[:-1])
y = ""
for i in z :
    if int(i)%2 == 1 :
        y = y + i + " "
print(y[:-1]) 



'''
n = int(input())
s = str(n)
z = ""
for i in s:
  if int(i)%2 == 0:
    z = z + i + " "
print(z[:-1])

for i in s:
  if int(i)%2 != 0:
    z = z + i + " "
print(z[:-1]) '''
