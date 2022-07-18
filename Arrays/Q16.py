n,w = map(int,input().split())
array = list(map(int,input().split()))

index_0 = []
start = 0
end = w
while start <= n-w:
  if 0 in array[start:end]:
    index_0.append(array.index(0,start)+1)
  else:
    index_0.append(-1)
  start += 1
  end += 1

print(*index_0)
