s = input()
odd_pos = ''
even_pos = ''
for i in range(1,len(s)+1):
    if i%2 == 0:
        even_pos += s[i-1]
    else:
        odd_pos += s[i-1]

print(odd_pos+" "+even_pos)
