s = input()
count = 0
for char in sorted(s):
    if s.count(char) <= 1:
        count+=1
if count > 0:
    print(count)
else:
    print(-1)
