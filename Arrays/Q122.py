str1,str2 = input().split()

if len(str1) != len(str2) :
    print('no')
else:
    dictionary = {}
    for i in range(len(str1)):
        if str1[i] in dictionary.keys() or str2[i] in dictionary.keys():
            try:
                if dictionary[str1[i]] != str2[i] or dictionary[str2[i]] != str1[i]:
                    print('no')
                    break
            except KeyError :
                print('no')
                break
        else:
            dictionary[str1[i]] = str2[i]
            dictionary[str2[i]] = str1[i]
    else:
        print('yes')
