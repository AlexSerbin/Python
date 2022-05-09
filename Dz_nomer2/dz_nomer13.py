stroka = input("Введите строку ")
k = stroka.find("h")   # индекс первой
j = stroka.rfind("h")  # индекс последней
str2 = stroka[:k+1:] + stroka[k+1:j:].replace('h', 'H') + stroka[j::]
print(str2)
