a,b = input().split()
sum = ''
for n,i in enumerate(a):
    for j in b[n:]:
        sum += str((int(i) + int(j))%10)
        break

print(sum)
