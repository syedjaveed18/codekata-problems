n = int(input())

def prime(n):
    if n == 1 or n == 0:
        return None
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        return n

hyp_list = []
number = 0
while len(hyp_list) < n:
    condition = True
    for i in str(number):
        if prime(int(i)):
            pass
        else:
            condition = False
    
    if condition:
        hyp_list.append(number)
    
    number += 1

print(hyp_list[-1])
