n = int(input())
array = list(map(int,input().split()))

lcm = max(array)
while True:
    count = 0
    for elem in array:
        if lcm%elem == 0:
            count += 1
    if count == len(array):
        break
    lcm += 1

print(lcm)
