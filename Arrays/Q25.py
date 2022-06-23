no_of_arrays = int(input())
output = []
for n in range(no_of_arrays):
    size = int(input())
    array = list(map(int,input().split()))
    array.sort()
    output.extend(array)

print(" ".join([str(elem) for elem in output]))
