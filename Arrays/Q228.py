Encrypted_string = input()

if '[' in Encrypted_string:
    Encrypted_string1 = Encrypted_string.split('[')
    Encrypted_string1[-1] = Encrypted_string1[-1][:Encrypted_string1[-1].count(']') - 1]
    Encrypted_string1

    Decrypted_string = ''

    for char in Encrypted_string1[::-1]:
        if char.isdigit():
            Decrypted_string = Decrypted_string*int(char)
        else:
            Decrypted_string = char + Decrypted_string

    print(Decrypted_string)
else:
    print(Encrypted_string)
