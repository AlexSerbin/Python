ver = hor = 11
# ━ ┃ ┣ ┫  ┛ ┗ ┓ ┏ ┳ ┻  ╋ │ ┤
for i in range(ver):
    for k in range(hor):
        if i == 0 and k == hor - 1:
            print('━┓', end='')
        elif k == 0 and i == 0:
            print('┏━', end='')
        elif k == 0 and i == ver - 1:
            print('┗━', end='')
        elif k == 0:
            print('┣━', end='')
        elif k == hor - 1 and i == ver - 1:
            print('━┛', end='')
        elif k == hor - 1:
            print('━┫',end='')
        elif i == ver - 1:
            print('━┻━',end='')
        elif i == 0:
            print('━┳━',end='')
        else:
            print('━╋━', end='')
    print()
