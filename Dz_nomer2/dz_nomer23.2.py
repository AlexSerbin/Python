text = input('Введите текст ')

d = {}
for word in text.lower().split():
    d[word] = d.get(word, 0) + 1
last = 0
for key in d:
    if d.get(key) == max(d.values()):
        last = key

print('Слово которое встречается чаще всего: ', last)



