'''s = str(input())
i = 0
for val in s :
    if val == " ":
        continue
    else:
        i=i+1

print(i) '''

s = str(input())
z = s.replace(" ", "")
#print(z)
print(len(z))
