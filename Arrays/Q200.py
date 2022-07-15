N = int(input())

while N > 0:
    s = ""
    for i in range(N):
        s = s + "1" + " "
    print(s[:-1])
    N = N -1
