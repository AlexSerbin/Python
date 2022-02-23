ver = hor = 21

# ━ ┃ ┣ ┫  ┛ ┗ ┓ ┏ ┳ ┻  ╋ │ ┤ ▅   ▀▀▄▅▆▇█▉▊▋  ▉
b = []
for i in range(ver):
    for k in range(hor):
        if i == 0 and k == hor - 1:
            print('━┓', end='')
            b.append('━┓')
        elif k == 0 and i == 0:
            print('┏━', end='')
            b.append('┏━')
        elif k == 0 and i == ver - 1:
            print('┗━', end='')
            b.append('┗━')
        elif k == 0 and i % 2 == 0:
            print('┣━', end='')
            b.append('┣━')
        elif k == 0:
            print('┃ ', end='')
            b.append('┃ ')
        elif k == hor - 1 and i == ver - 1:
            print('━┛', end='')
            b.append('━┛')
        elif k == hor - 1 and i % 2 == 0:
            print('━┫',end='')
            b.append('━┫')
        elif k == hor - 1:
            print(' ┃',end='')
            b.append(' ┃')
        elif i == ver - 1 and k % 2 == 0:
            print('━┻━',end='')
            b.append('━┻━')
        elif i == 0 and k % 2 == 0:
            print('━┳━',end='')
            b.append('━┳━')
        elif i == 0 or i % 2 == 0 and k % 2 == 1 or i == ver - 1:
            print('━━━',end='')
            b.append('━━━')
        elif i % 2 == 1 and k % 2 == 1:
            print('   ',end='')
            b.append('   ')
        elif i % 2 == 1 and k % 2 == 0:
            print(' ┃ ',end='')
            b.append(' ┃ ')
        else:
            print('━╋━', end='')
            b.append('━╋━')
    print()
    b.append('\n')
# k = 0
# for i in range(len(b)):
#     if b[i] == '   ':
#         print(i)
#         k +=1
# print(k)


b[23] = "███"
print (''.join(b))
