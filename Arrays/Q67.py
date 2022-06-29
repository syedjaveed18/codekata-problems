n = int(input())

def sorting(x):
    return "".join(sorted(x))
    
anagram = sorting('kabali')

list_s = []
for i in range(n):
    s = input()
    list_s.append(sorting(s))

count = 0
for string in list_s:
    if string == anagram:
        count += 1

if count > 0:
    print(count)
else:
    print(0)
