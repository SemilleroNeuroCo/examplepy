def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def division(x,y):
    if y == 0:
        raise ValueError

    return x/y

def power(x,y):
    return x**y