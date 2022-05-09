from random import randint

#lst = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]   #удобный список
lst = []
for _ in range(15):
    lst.append(randint(1, 15))
print('Рандомный списочек: ', lst)

k = 0
for i in range(1, (len(lst)-1)):
    if lst[i] > lst[i+1] and lst[i] > lst[i-1]:
        k += 1

if k == 0:
    print('Нет элементов которые больше двух своих соседей')
else:
    print("Количество элементов которые больше своих соседей:", k)