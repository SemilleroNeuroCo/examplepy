def suma(x,y):
    """Sumar dos números x,y

    Parameters
    ----------
    x : Numeric
    y : Numeric
    
    Returns
    -------
    Numeric
        Suma de los números
    """
    return x+y

def resta(x,y):
    """Resta dos números x,y

    Parameters
    ----------
    x : Numeric
    y : Numeric
    
    Returns
    -------
    Numeric
        Resta de los números
    """

    return x-y

def multiplicacion(x,y):
    """Multiplicación dos números x,y

    Parameters
    ----------
    x : Numeric
    y : Numeric
    
    Returns
    -------
    Numeric
        Multiplicación de los números
    """

    return x*y

def division(x,y):
    """División dos números x,y

    Parameters
    ----------
    x : Numeric
    y : Numeric
    
    Returns
    -------
    Numeric
        División de los números
    """

    if y == 0:
        raise ValueError

    return x/y

def power(x,y):
    """Elevar x a la y

    Parameters
    ----------
    x : Numeric
    y : Numeric
    
    Returns
    -------
    Numeric
        Potencia x**y
    """

    return x**y