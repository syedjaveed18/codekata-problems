n = int(input())
array = list(map(int,input().split()))

repeated_twice = ' '
for elem in set(array):
    if array.count(elem) == 2:
        repeated_twice = repeated_twice + str(elem) + ' '

print(repeated_twice[:-1])
