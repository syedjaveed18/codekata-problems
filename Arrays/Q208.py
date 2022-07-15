m = int(input())
arr1 = list(map(int,input().split()))
n = int(input())
arr2 = list(map(int,input().split()))

arr1.extend(arr2)
union = list(set(arr1))
union.sort()

print(*union)
