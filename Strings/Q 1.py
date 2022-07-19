s = input()
result_string = ''

for i in s:
    if s.count(i) == 1:
        result_string += i

print(result_string)
