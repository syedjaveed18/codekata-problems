A = int(input())

notes_list = [1000,500,100,50,10,1]

sum = 0
no_of_notes = 0

while sum <= A:
  for i in notes_list:
    if (sum + i) <= A:
      sum = sum + i
      no_of_notes += 1
  if sum == A:
    break

print(no_of_notes)
