x = int(input("введите трехзначное число "))
if  x < 100 or x > 999:
    print("просили же ввести трехзначное число...")
else:
    a = x % 10              # третье число
    b = x % 100 // 10       # второе число
    c = x % 1000 // 100     # первое число
    print( "развернули - ", a * 100 + b * 10 + c)
