stroka = input("Введите строку ")
sym = input("Введите символ который хотите найти ")
k = 0
"""
while k < len(stroka):
    k = stroka.find(sym, k)
    if k == -1:
        break
    print(sym, "=", "[", k, "]")
    k = k + 1

"""
x = 0                                       #чисто для красоты выводов
#while k < len(stroka):
for k in range(len(stroka)):
    if k == 0:
        x = stroka.find(sym)
        print("Индексы символов ", end="")
    else:
        x = stroka.find(sym, x + 1)
    if x == -1 and k == 0:
        print("не найдены".lower())
    if x == -1:
        break
    print(x, end=' ')
    k = k + 1




