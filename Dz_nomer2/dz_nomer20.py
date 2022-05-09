ver = int(input('Введите высоту фигуры '))
hor = ver * 2 - 1

for i in range(ver):
    for k in range(hor):
        if hor//2 - i <= k <= hor//2 + i:
            print('*  ', end="")
        else:
            print('   ', end='')
    print()

