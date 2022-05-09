ver = int(input('Введите высоту фигуры '))
hor = ver * 2 - 1

for i in range(ver):
    for k in range(hor):
        if i == ver - 1 or i == ver - 1 - k or k == hor//2 + i:
            print('*  ', end="")
        else:
            print('   ', end='')
    print()

