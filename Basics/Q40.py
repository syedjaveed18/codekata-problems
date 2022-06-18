n = int(input())
roman_army = list(map(int,input().split()))
weak = 0

for i in range(n-2):
    if roman_army[i] > roman_army[i+1] > roman_army[i+2]:
        weak += 1

print(weak)
