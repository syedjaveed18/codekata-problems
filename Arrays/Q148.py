n = int(input())
array = list(map(int,input().split()))

suffix_sum = [sum(array[i:]) for i in range(n)]

print(*suffix_sum)
