n = input()
arr = input().split()
for i in range(0,len(arr),2):
    try:
        arr[i],arr[i+1] = arr[i+1],arr[i]
    except:
        continue
print(' '.join(arr))
