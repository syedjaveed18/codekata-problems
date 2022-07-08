n = int(input())
vowels = ['a','e','i','o','u']
strings = []

for i in range(n):
    string = input()
    strings.append(string)

length = list(map(len,strings))

def vowels_count(string):
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

no_of_vowels = list(map(vowels_count,strings))
new_string = []

max_vowels = max(no_of_vowels)
while max_vowels >= min(no_of_vowels):
  if max_vowels in no_of_vowels and no_of_vowels.count(max_vowels) > 1:
    index = no_of_vowels.index(max_vowels)
    for i in range(no_of_vowels.count(max_vowels)):
      new_string.append(strings[index])
      index += 1
  else:
    new_string.append(strings[no_of_vowels.index(max_vowels)])
  max_vowels -= 1

for elem in new_string:
    print(elem)
