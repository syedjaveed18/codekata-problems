n = int(input())
usernames = input().split()

output = []
i = 1
for username in usernames:
    if usernames[:i].count(username) > 1:
        output.append(username+'1')
    else:
        output.append('Verified')
    i += 1

print(*output)
