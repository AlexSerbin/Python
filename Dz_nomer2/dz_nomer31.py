from string import ascii_uppercase

n = int(input('Введите число '))
system = int(input('Система исч в которую хотите перевести '))
b = []

while n > 0:
    if n % system >= 10:
        b.insert(0, ascii_uppercase[n % system - 10])
    else:
        b.insert(0, n % system)
    n = n // system

z = ''.join(str(val) for val in b)

print('Число в {}-ой системе исчесления = {}'.format(system, z))
