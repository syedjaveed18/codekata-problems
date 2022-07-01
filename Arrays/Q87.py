n = int(input())

def binary(n):
    binary_num = ""
    while n>0:
        rem = n%2
        n = n//2
        binary_num = binary_num + str(rem)
    return binary_num[::-1]
    
print(binary(n).count('1'))
