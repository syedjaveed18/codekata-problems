number = list(input())
for i,j in enumerate(number):
  if i <= len(number) - 2:
    if number[i] == number[i+1]:
      number.remove(j)
      number.remove(j)

if len(number) == 0:
    print(-1)
else:
    print("".join(number))
