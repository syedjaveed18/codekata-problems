n = input()
arr = input()
sum_elements = sum(list(map(int,arr.split(" "))))
if sum_elements%2 == 0 and sum_elements%3 == 0 and sum_elements%3 == 0:
    print(1)
else:
    print(0)
