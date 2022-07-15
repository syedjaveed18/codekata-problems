n = input()
numbers = list(map(int,input().split()))

m = 0
count = 0
for i in numbers[:-2]:
    m += 1
    for j in numbers[m:-1]:
        if i+j in numbers[m+1:]:
            count+=1

print(count)
