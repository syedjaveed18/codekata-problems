n = input()
die = list(map(int,input().split()))
for i in die:
    if die.count(i) > 1:
        continue
    else:
        print(i)
