string,k = input().split()

new_string = ''

if int(k) == 0:
    print(string)
else:
    for i in range(1,len(string)+1):
        if i%int(k) == 0:
            new_string += string[i-1].upper()
        else:
            new_string += string[i-1]
    print(new_string)
