n = int(input())
array = list(map(int,input().split()))

def product_array(array):
    product = 1
    for elem in array:
        product *= elem
    return product

out = []
for elem in array:
    array_copy = array.copy()
    array_copy.remove(elem)
    out.append(product_array(array_copy))

print(*out)
