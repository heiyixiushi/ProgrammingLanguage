# -*- coding: utf-8 -*-
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, city = extra['city'], job=extra['job'])
person("Jack", 24, **extra)