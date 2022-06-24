m,n = map(int,input().split())
ram = 0
sita = 0
for i in range(m):
    result = list(map(int,input().split()))
    ram = ram + result.count(0)
    sita = sita + result.count(1)

print("RAM:",ram)
print("SITA:",sita)
