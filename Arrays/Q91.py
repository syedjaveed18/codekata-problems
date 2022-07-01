n = int(input())
n_integers = input().split()
weights = list(map(int,input().split()))

weigths_sorted = sorted(weights)

array_based_on_weights = []
for i in weigths_sorted:
    array_based_on_weights.append(n_integers[weights.index(i)])

print(" ".join(array_based_on_weights))
