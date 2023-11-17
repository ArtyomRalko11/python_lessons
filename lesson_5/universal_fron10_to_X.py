num = int(input('Input decimal number: '))

base = int(input('Enter base:'))
res = ''

while num != 0:
    rem = num % base
    num //= base
    res = str(rem) + res
    
print(res)