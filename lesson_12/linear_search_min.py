import random as r

lst = []
for i in range(50):
    lst.append(r.randint(1,299))

min_num = lst[0]
print(lst)
for i in range(len(lst)):
    if lst[i] < min_num:
        min_num = lst[i]

print('Smallest number: ', min_num, ", index:", lst.index(min_num))