binary = input()
power = len(binary) - 1

decimal = 0
for i in binary:
    decimal += (2**(power))*int(i)
    power -= 1
#print(decimal)

octal = ''
while decimal > 0:
    octal += str(decimal%8)
    decimal //= 8

print(octal[::-1])
