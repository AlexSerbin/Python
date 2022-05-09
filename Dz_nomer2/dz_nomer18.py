from random import randint

lst = []
for _ in range(15):
    lst.append(randint(1, 15))
print('Список 1: ', lst)

lst2 = []
for _ in range(15):
    lst2.append(randint(1, 15))
print('Список 2: ', lst2)


print("Количество уникальных чисел одномвременно в двух списка: ", len(set(lst) ^ set(lst2)))
