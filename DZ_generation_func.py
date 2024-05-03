# -*- coding: UTF-8 -*-

#Fabric_func
def operation(oper):
    if oper == 'add':
        def add(x, y):
            return x + y
        return add
    elif oper == 'multip':
        def multip(x, y):
            return x * y
        return multip
    else:
        raise 'Вы выбрали не верную функцию'

my_func = operation('add')
print(my_func(2, 4))
my_func_2 = operation('multip')
print(my_func_2(x=7, y=3))
# my_func_3 = operation('odd')
# print(my_func_3(4, 8))


#Lambda_func
numbers = [ 3, 5, 4, 1, 8, 56, 34]
res = map(lambda x: x ** 2, numbers)
print(list(res))

def exponen(x):
    return x ** 2

res_2 = map(exponen, numbers)
print(list(res_2))

#Call_obj
class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

my_rectangle = Rect(4, 8)
print(my_rectangle.__call__())





