print('Координаты задаются латинской буквой и цифрой\n')
crdn = input("Введите координаты начала хода коня ").lower()
crdn1 = input("Введите координаты конца хода коня ").lower()
letters = "abcdefgh"
numb = "12345678"
if len(crdn) == 2 and crdn[0] in letters and crdn[1] in numb:  # Валлидность первой клетки (a1-h8)
    x = crdn[0]
    y = int(crdn[1])

else:
    print("Неверные координаты 1")
    exit()

if len(crdn1) == 2 and crdn1[0] in letters and crdn1[1] in numb:  # Валлидность второй клетки (a1-h8)
    x1 = crdn1[0]
    y1 = int(crdn1[1])

else:
    print("Неверные координаты 2")
    exit()

if (abs(ord(x) - ord(x1)) == 1 and abs(y - y1) == 2) or (abs(ord(x) - ord(x1)) == 2 and abs(y - y1) == 1):
        print("Конь делает прыжок и попадает на вторую клетку")
else:
        print("Конь так не пойдет")

