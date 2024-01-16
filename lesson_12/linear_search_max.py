import random as r

lst = []
for i in range(50):
    lst.append(r.randint(1,299))

max_num = lst[0]
print(lst)
for i in range(len(lst)):
    if lst[i] > max_num:
        max_num = lst[i]

print('Biggest number: ', max_num, ", index:", lst.index(max_num))