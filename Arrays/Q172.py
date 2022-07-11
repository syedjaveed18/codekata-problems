n = int(input())
numbers = set(map(int,input().split()))
actual_numbers = set(range(1,n+1))

print(*actual_numbers.difference(numbers))
