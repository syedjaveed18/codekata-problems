string,k = input().split()
new_string = ''

for i in range(int(k),len(string)+1,int(k)):
    new_string += string[i-1] + " "

print(new_string[:-1])
