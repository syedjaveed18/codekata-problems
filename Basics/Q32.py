string,shift = input().split()
shift = int(shift)

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

new_string = ''
for i in string:
    if i in uppercase:
        if (shift + uppercase.index(i)) > 25 :
            new_pos = (shift + uppercase.index(i) - 1)%25
        else:
            new_pos = (shift + uppercase.index(i))
        new_string += uppercase[new_pos]
    else:
        if (shift + lowercase.index(i)) > 25 :
            new_pos = (shift + lowercase.index(i) - 1)%25
        else:
            new_pos = (shift + lowercase.index(i))
        new_string += lowercase[new_pos]

print(new_string)
