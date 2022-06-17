a,b,c = map(int,input().split())
largest = max(a,b,c)
smallest = min(a,b,c)
if a != largest and smallest :
  other = a
if b != largest and smallest :
  other = b
if a != largest and smallest :
  other = c
#print("largest is ",largest,"smallest is ",smallest,"other is ",other)
if largest < smallest + other and largest > abs(other - smallest):
  print("yes")
else:
  print("no")
