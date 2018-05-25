# -*- coding: utf-8 -*-

def my_abs(x):
    if not  isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    return x if x >=0 else -x
print(my_abs(-4))