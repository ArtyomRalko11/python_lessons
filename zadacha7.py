n = int(input('введите число'))
m = []
res = 0
while n > 0:
    m.append(n % 10)
    n //= 10
i = 0
while i < len(m) - 1:
    if m[i] > m[i + 1] and m[i] > m[i - 1] and m[i] > res:
        res = m[i]
    i += 1

print(res)