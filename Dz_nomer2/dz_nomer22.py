ver = int(input('Введите высоту фигуры '))
if ver % 2 == 0:                         #условие тк нельзя построить равносторонний ромб по клеточкам с четной высотой
    ver = ver+1
hor = ver

for i in range(ver):
    for k in range(hor):
        if hor//2 - i <= k <= hor//2 + i and i <= ver//2 or k == hor//2 or k == i - hor//2 or i == hor - k + ver//2 -1:
            print('*  ', end="")
        else:
            print('   ', end='')
    print()


"""for i in range(ver):                  #специально для четной высоты для максимально корректной приближенной фигуры к ромбу     
    for k in range(hor):
        if hor//2 - i <= k <= hor//2 + i and k != 0 and i <= ver//2 or k == hor//2 or k == i - hor//2 + 1 and k !=0 or i == hor - k + ver//2 -1:
            print('*  ', end="")
        else:
            print('   ', end='')
    print()"""