import random as r

lst = []
for i in range(100):
    lst.append(r.randint(0, 10000))

lst.sort()
print(lst)

start = 0
stop = len(lst) - 1
mid = (start + stop) // 2
key = int(input('Number to search: '))

while (start <= stop and lst[mid] != key):
    if key < lst[mid]:
        stop = mid - 1
    elif key > lst[mid]:
        start = mid + 1
    mid = (start + stop) // 2

if key != lst[mid]:
    print('Not found')
else:
    print('Found on index', mid)