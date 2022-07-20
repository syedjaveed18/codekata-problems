PAN_number = input()

not_pan = False

if len(PAN_number) != 10:
    not_pan = True

for char in PAN_number[:5]:
    if char.islower() or not(char.isalpha()):
        not_pan = True
        break

if PAN_number[-1].islower() or not(PAN_number[-1].isalpha()):
    not_pan = True

for num in PAN_number[5:-1]:
    if not(num.isdigit()):
        not_pan = True
        break

if not_pan:
    print('not pan')
else:
    print('pan')
