string = input()

beautiful_string = True

if string[0] not in ['a','A'] or string[len(string)//2] not in ['m','M'] or string[-1] not in ['z','Z']:
    beautiful_string = False

if beautiful_string:
    print(1)
else:
    print(0)
