n,m = map(int,input().split())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

A1_relative_to_A2 = []

A1_copy = A1.copy()
for elem1 in A2:
    for elem2 in A1:
        if elem1 == elem2:
            A1_copy.remove(elem2)
            A1_relative_to_A2.append(elem2)

A1_copy.sort()
A1_relative_to_A2.extend(A1_copy)
print(*A1_relative_to_A2)
