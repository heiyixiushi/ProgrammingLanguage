# !/bin/python env
# -*= coding: utf-8 -*-
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24, city='Beijing', 'Engineer')