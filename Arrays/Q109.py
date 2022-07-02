s = input().split()
reverse_saturated = []

for i in s:
    reverse_saturated.append(i[::-1])
    
print(*reverse_saturated)
