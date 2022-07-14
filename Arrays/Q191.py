n,k = map(int,input().split())
n_elements = list(map(int,input().split()))
n_elements.sort()

print(n_elements[-k])
