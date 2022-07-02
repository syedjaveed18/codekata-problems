m = int(input())
array = list(map(int,input().split()))
initial_array = sorted(array)

if array == initial_array:
    print(-1)
else:
    for i in range(1,m+1):
        new_array = initial_array[-i:] + initial_array[:m-i]
        if new_array == array:
            print(i)
            break
