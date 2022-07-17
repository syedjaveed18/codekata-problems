n = int(input())
n_numbers = list(map(int,input().split()))

for i in n_numbers:
    n_numbers_copy = n_numbers.copy()
    n_numbers_copy.remove(i)
    if i in n_numbers_copy:
        print(i)
        break
else:
    print('unique')
