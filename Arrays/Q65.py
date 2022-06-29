n = int(input())
array = list(map(int,input().split()))
odd_even = []

for elem in array:
    odd_even.append(0) if elem%2 == 0 else odd_even.append(1)

if odd_even.count(1) > 1 and odd_even.count(0) == 1:
    print(array[odd_even.index(0)])
elif odd_even.count(0) > 1 and odd_even.count(1) == 1:
    print(array[odd_even.index(1)])
else:
    print(-1)
