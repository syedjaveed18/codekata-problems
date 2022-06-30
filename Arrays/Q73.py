s = input()
vowels = ['a','e','i','o','u']

without_vowels = ''
for i in s:
    if i not in vowels:
        without_vowels += i

if len(without_vowels) > 0:
    print(without_vowels[::-1])
else:
    print(-1)
