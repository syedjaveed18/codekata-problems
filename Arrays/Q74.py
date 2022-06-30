n = int(input())
binary = ''
while n > 0:
    rem = n%2
    n = n//2
    binary = binary + str(rem)
print(binary[::-1])
