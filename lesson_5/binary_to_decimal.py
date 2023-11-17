bin = input('Number:')
n = 0

for i in range(len(bin)):
    tmp=len(bin) - i - 1
    n += int(bin[i]) * pow(2, tmp)
    
print(n)
    
    