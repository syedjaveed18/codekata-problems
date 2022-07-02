n = int(input())
digits = [dig for dig in str(n)]
print(''.join([str(elem) for elem in sorted(digits, reverse=True)]))
