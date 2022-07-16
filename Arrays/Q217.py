n = int(input())
N_numbers = input().split()

for i in N_numbers:
    if N_numbers.count(i) == 1:
        print(i)
        break
