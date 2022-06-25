n = input()
die = list(map(int,input().split()))
c = 0
for i in die:
    if die.count(i) > 1:
        continue
    else:
        print(i)
        c += 1

if c == 0:
    print(0)
