n = int(input())
li = [2]
diff = 3
while len(li) < n:
    li.append(li[-1]+diff)
    diff+=2
#print(" ".join([str(elem) for elem in li]))
print(*li)
