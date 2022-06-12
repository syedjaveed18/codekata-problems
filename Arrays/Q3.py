n = int(input())
array = input()
k = int(input())
s = ""
for i in array.split(" "):
    if int(i) < 0:
        s = s + i + " "
        break
for i in array.split(" "):
    if int(i) < 0:
        s = s + i + " "
if len(s) > 0:
    print(s[:-1])
else:
    z = '0 '*5
    print(z[:-1])
