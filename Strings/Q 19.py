s = list(input())
if len(s)%2 == 0:
    s[int(len(s)//2)] = '*'
    s[int(len(s)//2) - 1] = '*'
else:
    s[int(len(s)//2)] = '*'
    
print("".join(s))
