n = int(input())
elements = input()
zeros = elements.count('0')
if zeros < 2:
    print(-1)
else:
    left = elements.index('0')
    right = len(elements) - elements[::-1].index('0')
    output = ''
    for elem in elements[left:right]:
        if elem == '1':
            output += elem + ' '
    print(output[:-1])
