n,k = map(int,input().split())
array = list(map(int,input().split()))

diff = 1
array_copy = array.copy()
array.remove(k)

neighbours = []
while len(neighbours) <= 3:
    for elem in array_copy:
        if abs(elem - k) == diff:
            neighbours.append(elem)
            array_copy.remove(elem)
    diff += 1

print(*neighbours[:3])
