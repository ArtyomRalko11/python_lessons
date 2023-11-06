word = input("Введите строку: ")
symbol = input("Введите символ: ")
res = 0
for i in range (len(word)):
    if word[i] == symbol:
        res += 1 
    
    
print("В слове" ,word ,"символ",symbol, "встречается" ,res , "раз(а)")
        