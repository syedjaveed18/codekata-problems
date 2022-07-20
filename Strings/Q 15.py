string = input()

insert_char = 0
for i in range(len(string)-2):
    if len(set(string[i:i+3])) == 1:
        insert_char += 1

print(insert_char)
