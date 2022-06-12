n = int(input())
passport_num = input().split()
for elem in passport_num:
    passport_num_copy = passport_num.copy()
    passport_num_copy.remove(elem)
    if elem in passport_num_copy:
        passport_num[::-1].remove(elem)
passport_num.sort()
print(" ".join([elem for elem in passport_num]))
