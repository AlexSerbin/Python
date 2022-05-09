s = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

print('Номер заказа, стоимость')
#print(list(map(lambda num, prc: (num, prc), list(map(lambda num: num[0], s)), list(map(lambda prc: round(prc[3] * prc[2] + 10 if prc[3] * prc[2] < 100 else prc[3] * prc[2], 2), s)))))


print(list(map(lambda num, prc:  ((num[0]), (round(prc[3] * prc[2] + 10 if prc[3] * prc[2] < 100 else prc[3] * prc[2], 2))), s, s)))



