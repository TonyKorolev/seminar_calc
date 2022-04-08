# Модуль математических операций с рациональными числами.
import math

x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b



def razi_sum():
    return x + y

def razi_mult():
    return x * y

def razi_sub():
    return x - y

def razi_dif():
    return x / y

def do_it(char):
    if char == '+':
        return round(x + y, 3)
    elif char == '-':
        return round(x - y, 3)
    elif char == '*':
        return round(x * y, 3)
    elif char == '/':
        return round(x / y, 3)

