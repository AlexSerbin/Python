N = int(input('Введите целое число: '))
for k in range(1, N):
    if (k**2) > N:
        break
    print(k ** 2, end=" ")


