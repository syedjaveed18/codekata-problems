n = int(input())
array = list(map(int,input().split()))
unique_elements = list(set(array))
frequency = []

for i in unique_elements:
    frequency.append(array.count(i))

print(unique_elements[frequency.index(max(frequency))])
