# s = '[31, 40, 14, 39, 50, 50, 42, 24, 22, 888, 28, 18, 30, 34]'
# lst_str = s.strip('[]').split(', ')
# print(lst_str)
#
# str_res = ' + '.join(lst_str)
# print(str_res, '=', eval(str_res))
#
# lst_int = [int(value) for value in lst_str]
# print(lst_int)
# print(sum([int(value) for value in lst_str]))
#
# str_line = ' - '.join([str(value) for value in lst_int])
# print(str_line, '=', eval(str_line))

# b = [[1,2,3],
#      [3,4,5],
#      [4,6,7,7]]
#
# #z =''.join([str(value) for value in b[1]])
# print(''.join([str(value) for value in b[1]]))
# print(b[2])
from pprint import pprint


class Demo:
    a = 0
    b = 0
    c = 0
    def __init__(self,A,B,C):
        self.a = A
        self.b = B
        self.c = C
    def display(self):
        print(self.a, self.b, self.c)
    def sosat(self, x):
        x = x + 1
        return x

x = 0
class Newdemo(Demo):
    d = 0
    x = 0
    def __init__(self,A,B,C,D,):
        self.d = D

        super().__init__(A,B,C)#super to call super Class
        #The __init__() Method
        super().sosat(x)

    def display(self):
        print(self.a, self.b, self.c,self.d)

B1 = Demo(12,34,56)
print("Contents of Base Class:")
B1.display()
D1 = Newdemo(1,2,3,4)
print("Contents of Derived Class:")
D1.display()
print(D1.sosat(4))

print(D1.__class__.__doc__)


def f(x) -> 1111:
    return x

print(f.__annotations__)


def enlight(hope: bool):
    return print('Lumos -', 'there is a hope' if hope else 'No hope')

enlight(True)

#print('Lumos -', enlight(True))
