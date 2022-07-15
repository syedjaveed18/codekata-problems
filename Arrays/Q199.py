n = int(input())
N_numbers = list(map(int,input().split()))

max_count = len(N_numbers)
flag = False
while True:
    for elem in set(N_numbers):
        if N_numbers.count(elem) == max_count:
            print(elem)
            flag = True
            break
    if flag:
        break
    max_count -= 1
