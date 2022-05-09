lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""                       #ручное наполнение списка
lst = []
n = int(input('Введите длину списка '))

for i in range(n):
    print('Элемент[', i+1, ']: ', end="")
    lst.append(int(input()))
"""

print('Ваш список', lst)

for i in range(len(lst)//2):
    lst[i], lst[-i-1] = lst[-i - 1], lst[i]

print('Разворот', lst)