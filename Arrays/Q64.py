n = int(input())
n_elements = list(map(int,input().split()))
n_elements.remove(min(n_elements))

if len(set(n_elements)) == 1:
    print(-1)
else:
    print(min(n_elements))
