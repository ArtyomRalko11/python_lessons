text = input('Сообщение:')
shift = int(input('Сдвиг шифра: '))
encrypted = ''

for char in text:
    if char.isalpha():
        shift_amount = shift % 26
        if char.islower():
            shifted_char = chr(((ord(char) - ord('a') + shift_amount)% 26) + ord('a'))
        else:
            shifted_char = chr(((ord(char) - ord('A') + shift_amount)% 26) + ord('A'))
        encrypted += shifted_char
    else:
        encrypted += char
print(encrypted)

for shift in range(1, 27):
    decrypted = ''
    for char in encrypted:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') - shift_amount)% 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') - shift_amount)% 26) + ord('A'))
            decrypted += shifted_char
        else:
            decrypted += char
    print(f' Test {shift}: {decrypted}')