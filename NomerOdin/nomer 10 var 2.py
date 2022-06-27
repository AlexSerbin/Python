ver = int(input('Введите высоту грани '))
ver = ver + ver//2
if ver % 3 == 0:
    ver = ver + 1
    print("Общая высота фигуры не может быть кратной 3, увеличиваем высоту ну 1\n")

for i in range(ver):
    for k in range(ver):
        if k == 0 and i >= ver // 3 or k <= 2 * ver // 3 and i == ver // 3 or k == 2 * ver // 3 and i >= ver // 3 \
                or k <= 2 * ver // 3 and i == ver - 1 or i == ver // 3 - k or k >= ver // 3 and i == 0 \
                or k == ver - 1 and i <= 2 * ver // 3 or i == ver - 1 - k and i < ver // 3 \
                or i == ver - 1 - k + 2 * ver // 3:
            print('*  ', end='')
        else:
            if k == ver // 3 and i < 2 * ver // 3 or k >= ver // 3 and i == 2 * ver // 3 \
                    or i == ver - 1 - k and 0 <= k < ver // 3:
                print('-  ', end='')
            else:
                print('   ', end='')
    print()
