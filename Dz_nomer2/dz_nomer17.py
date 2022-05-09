from random import randint

lst = []
for _ in range(15):
    lst.append(randint(1, 15))
print('Рандомный списочек: ', lst)

print("Уникальных значений: ", len(set(lst)))

