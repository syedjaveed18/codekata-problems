s = str(input())
x = "aeiouAEIOU"
for i in s:
  if i in x:
    print("yes")
    break
else:
  print("no")
