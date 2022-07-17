n = int(input())
array = input().split()
u,v = input().split()

def indices(array,elem):
  index_array = []
  pos = 0
  while True:
    if elem in array[pos:]:
      index_elem = array.index(elem,pos)
      index_array.append(index_elem)
      pos += index_elem + 1
    else:
      break

  return index_array

indices_of_u = indices(array,u)
indices_of_v = indices(array,v)

distance = []
for pos1 in indices_of_u:
  for pos2 in indices_of_v:
    distance.append(abs(pos1 - pos2))

print(min(distance))
