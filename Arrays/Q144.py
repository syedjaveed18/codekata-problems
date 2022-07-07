n = int(input())

string_list = []
for i in range(n):
    s = input()
    string_list.append(s)

string_list.sort()
print(string_list[0])
