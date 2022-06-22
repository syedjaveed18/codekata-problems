a,b,c = map(int,input().split())
largest = max(a,b,c)
smallest = min(a,b,c)
if a != largest and smallest :
  other = a
if b != largest and smallest :
  other = b
if a != largest and smallest :
  other = c
if a==b or b==c or a==c :
    print("no")
else:
    if largest < smallest + other and largest > abs(other - smallest):
        print("yes")
    else:
        print("no")
