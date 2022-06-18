y = int(input())
numbers = list(map(int,input().split()))
t = int(input())
t_num = list(map(int,input().split()))
occurance_of_number = []
for num in t_num:
    if numbers.count(num) >= 1:
        occurance_of_number.append(numbers.count(num))
    else:
        occurance_of_number.append('Not Present')
print(' '.join([str(elem) for elem in occurance_of_number]))
