n = int(input())
numbers = list(map(int,input().split()))
print(numbers.index(min(numbers))+1,numbers.index(max(numbers))+1)
