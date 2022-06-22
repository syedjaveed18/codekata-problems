N = input()
pow = len(N) - 1
dec = 0
for i in N:
    dec = dec + int(i)*2**pow
    pow = pow - 1

print(dec)
