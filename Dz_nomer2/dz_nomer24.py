def arithmetic(a, b, c):
    if c == "+":
        return a + b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    elif c == "-":
        return a - b
    return "Unknown operation"


first = int(input("Введите первое число "))
second = int(input("Введите второе число "))
oper = input("введите операцию символом ")

print('Ответ ', arithmetic(first, second, oper))
