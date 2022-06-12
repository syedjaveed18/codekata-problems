len1,diff = map(int,input().split())
arr = input()
li = arr.split(" ")
li = li + li[0:1]
s = ""
for i in range(0,len1):
    if abs(int(li[i+1])-int(li[i])) > diff:
        s = s+'1'+" "
    else:
        s = s+'0'+" "
print(s[:-1])
