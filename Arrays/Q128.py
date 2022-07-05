n,k = map(int,input().split())
n_elements = list(map(int,input().split()))
k_elements = list(map(int,input().split()))

max_elements = []
for k in k_elements:
    n_elements.append(k)
    max_elements.append(max(n_elements))

print(*max_elements)
