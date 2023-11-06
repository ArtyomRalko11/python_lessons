word = input("Введите слово: ")
big_let = " "

for i in range(len(word)):
    #print(word[c])
    #print(big_let)
    if word[i] > big_let:
        big_let = word[i]
    
    #print(c)
print(big_let)