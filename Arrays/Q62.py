array = list(map(int,input().split()))
new_array = []
while len(array) > 0:
    try:
        new_array.append(max(array))
        array.remove(max(array))
        new_array.append(min(array))
        array.remove(min(array))
    except:
        pass

print(" ".join([str(i) for i in new_array]))
