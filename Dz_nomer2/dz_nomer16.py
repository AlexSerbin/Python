print('Введите элементы списка через пробел: ', end="")
lst = list(map(int, input().split()))
k = int(input('введите индекс искомго элемента: '))
if k > len(lst):
    print("Индекс за пределами списка")
    exit()
print("Ваш список    ", lst)
print("Элемент который удаляем ", lst[k])

for i in range(k, (len(lst)-1)):
    lst[i], lst[i+1] = lst[i+1], lst[i]

lst.pop()
print("Список без эл.", lst)
