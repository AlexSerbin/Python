lines = int(input('Введите количество строк текста '))
lst = []
print("Введите текст")
for _ in range(lines):
    lst.extend((input()).lower().split())
print(lst)
counter = 0
maxx = 0
counter2 = 0
a = 0
dic = {i: lst[i] for i in range(len(lst))}

print(dic)

for i in range(len(dic)):
    for k in range(len(dic)):
        if dic.get(i) == dic.get(k):
           counter += 1
    if counter >= counter2:
        maxx = dic.get(i)
        counter2 = counter
    counter = 0
print("Слово которое встречается чаще всего -", maxx)








