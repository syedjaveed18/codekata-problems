n = int(input())
array = input().split()
array_sort = sorted(array)

if array_sort == array or array_sort == array[::-1]:
    print('yes')
else:
    print('no')
