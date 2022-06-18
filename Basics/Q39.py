a,b = input().split()
if (a == 'R' and b == 'P') or (a == 'P' and b == 'R'):
    print("P")
elif (a == 'R' and b == 'S') or (a == 'S' and b == 'R'):
    print("R")
elif (a == 'P' and b == 'S') or (a == 'S' and b == 'P'):
    print("S")
elif (a == 'P' and b == 'P') or (a == 'S' and b == 'S') or (a=='R' and b=='R') :
    print("D")
