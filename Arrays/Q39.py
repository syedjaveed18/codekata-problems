n = int(input())
l = []
output = []
for i in range(n):
    query = list(map(int,input().split()))
    if query[0] == 1:
        l.append(query[-1])
    else:
        if len(l) == 0:
            output.append('-1')
        else:
            output.append(min(l))

print(" ".join([str(elem) for elem in output]))
