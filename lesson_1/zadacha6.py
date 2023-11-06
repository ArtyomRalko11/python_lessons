n = int(input('введите число'))
count = 0

while n > 0:
    res = n % 10
    if res == 1:
        count += 1
    n //= 10



print('В данном числе цифра 1 встречается', count, 'раз(а)')




