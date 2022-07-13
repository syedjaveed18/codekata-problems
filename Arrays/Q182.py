a,b = map(int,input().split())

def binary(n):
    binary_num = ""
    while n>0:
        rem = n%2
        n = n//2
        binary_num = binary_num + str(rem)
    return binary_num[::-1]
    
def prime(n):
    if n == 1:
        return None
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        return n

count = 0
for i in range(a,b+1):
    if prime(binary(i).count('1')):
        count += 1

print(count)
