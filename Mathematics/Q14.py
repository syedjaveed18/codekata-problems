n = int(input())
arr = input()
li_arr = list(map(int,arr.split(" ")))
s = ""
for elem in li_arr:
    if li_arr.count(elem) > 1:
        continue
    else:
        s = s+str(elem)+" "
print(s[:-1])
