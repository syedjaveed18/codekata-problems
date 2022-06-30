n,m = map(int,input().split())
numbers = input().split()

common_numbers = []
for i in range(n):
    if numbers[i] in numbers[-m:]:
        common_numbers.append(numbers[i])

common_numbers.sort()

print(" ".join(common_numbers))
