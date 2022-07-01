n = int(input())
n_elements = input().split()
max_of_consecutive = []

for i in range(n-1):
    max_of_consecutive.append(max(n_elements[i:i+2]))
    
print(" ".join(max_of_consecutive))
