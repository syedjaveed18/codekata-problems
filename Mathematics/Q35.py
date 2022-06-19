s = str(input())
s = s.replace('.','')
z = []
for i in s.split() :
    if i.isdigit():
        z.append(int(i))
print(max(z))
