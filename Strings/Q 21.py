n = int(input())

pairs_of_string = []
for i in range(n):
    strings = input().split()
    pairs_of_string.append(strings)

flag = False
for index,string1 in enumerate(pairs_of_string):
    for string2 in pairs_of_string[index+1:]:
        if string1[0] == string2[1] and string2[0] == string1[1]:
            flag = True
            break
    if flag:
        break

print("YES") if flag else print('NO')
