n,k = map(int,input().split())
array = list(map(int,input().split()))

while k > 0:
    if k in array:
        print(k)
        break
    else:
        k -= 1

if k not in array:
    print(-1)
