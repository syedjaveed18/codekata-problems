n,k = map(int,input().split())
n_elements = list(map(int,input().split()))

unique_elem = list(set(n_elements))

if len(unique_elem) >= k:
    for i in range(1,k):
        unique_elem.remove(min(unique_elem))
    print(min(unique_elem))
else:
    print(-1)
