def season(a):
    if a == 12 or 1 <= a <= 2:
        return "Зима"
    elif 3 <= a <= 5:
        return "Весна"
    elif 6 <= a <= 8:
        return "Лето"
    elif 9 <= a <= 11:
        return "Осень"
    return "В году 12 месяцев"


month = int(input('Введите номер месяца чтоб узнать пору года '))
print(season(month))
