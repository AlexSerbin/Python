s = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def costs(order):
    cost = round(order[3] * order[2], 2)
    if cost < 100:
        cost += 10
    return order[0], cost


d = [costs(s[i]) for i in range(len(s))]
print(d)

a = lambda order: round(order[3] * order[2], 2) + 10 if round(order[3] * order[2], 2) < 100 else round(order[3] * order[2], 2)
print(a(s[0]))
l = list(map(a, s))
print(l)


# x = list(map(lambda x: x[0], s))

z = zip(list(map(lambda x: x[0], s)), list(map(lambda order: round(order[3] * order[2], 2) + 10 if round(order[3] * order[2], 2) < 100 else round(order[3] * order[2], 2), s)))
print(list(z))





