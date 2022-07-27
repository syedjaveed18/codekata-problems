s1,s2 = input().split()

if s1 == s1[::-1] and s2 == s2[::-1] and sorted(s1) == sorted(s2):
    print(1)
else:
    print(0)
