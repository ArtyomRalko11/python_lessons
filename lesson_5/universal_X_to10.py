num = int(input('Input binary number: '))

base = int(input('Enter base:'))
res = 0

while i != 0:
    
   res = res* base + int(num[i])
   i += 1
print(res)