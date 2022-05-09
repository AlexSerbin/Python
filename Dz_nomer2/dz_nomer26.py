def is_year_leap(x):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    else:
        return False


year = int(input('Введите год если хотите узнать высокосный ли он '))
print(is_year_leap(year))