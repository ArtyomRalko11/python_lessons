n = int(input('Введите число:'))
temp = n
res = 1
i = 1
n2 = n
if n <= 0:
    print('Ошибка!')
while i < n2 - 1:
    temp = n - 1
    n = temp
    res *= temp
    i += 1

print(res * n2)



