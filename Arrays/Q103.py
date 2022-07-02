t = int(input())

package_number = []
for test_cases in range(t):
    n = int(input())
    batch_A = input().split()
    batch_B = input().split()
    removed_element = list(set(batch_A) - set(batch_B))
    package_number.append(batch_A.index(removed_element[0]))
    
for index in package_number:
    print(index)
