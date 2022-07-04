n = int(input())
numbers = list(map(int,input().split()))
for i in range(1,min(numbers)+1):
    for num in numbers:
        if num%i != 0:
            break

if i >= 2 :
    print(i)
else:
    print(-1)
