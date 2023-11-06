n = int(input('Введите число:'))
i = 0

while n > i:
    n = n % 10
    i += 1


print(i)