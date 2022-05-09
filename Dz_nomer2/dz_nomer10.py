k = 0
summa = 0
minimum = float('inf')
maximum = float('-inf')
chet = 0
nechet = 0

while True:
    N = int(input("Введите целое число: "))
    if N == 0:
        break

    if N > maximum:
        maximum = N

    if N < minimum:
        minimum = N

    if N % 2 == 0:
        chet += 1
    else:
        nechet += 1

    k += 1
    summa = N + summa


print("Количество введённых чисел: ", k)
print("Сумма чисел: ", summa)
print("Среднее арифметическое всех введённых чисел: ", summa/k)
print("Минимальное значение: ", minimum)
print("Максимальное значение: ", maximum)
print("Количество чётных значений: ", chet)
print("Колчичество нечётных значений: ", nechet)
