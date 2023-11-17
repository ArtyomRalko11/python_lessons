num = int(input('Введите число:'))
bin_num = ''

while num != 0:
    
    rem = num % 2
    num //= 2
    bin_num = str(rem) + bin_num
    
print(bin_num)