def f(x):
    """
    Función que evalua la función en un punto.
    :param x: Punto de evaluación.
    :return: Valor numérico de la evaluación.
    """
    return x**3 - 2*x**2 - 5


def bisection(maxit, erracep, a, b):
    """
    Función de busqueda de la raíz de una función, mediante la subdivisión de intervalos.
    :param maxit: Máximo número de iteraciones.
    :param erracep: Valor del error aceptado.
    :param a: Intervalo inferior.
    :param b: Intervalo superior.
    :return: Raíz de la función tal qué, f(valor) = 0; si esta cumple con las condiciones.
    """
    if f(a)*f(b) >= 0:
        print('¡La función no satisface la condición: f(a)*f(b) < 0!')
        return None
    else:
        i, cant = 0, 0.00
        c = (a + b) / 2
        erri = relerr(c, cant)
        while i < maxit and erri > erracep:
            if i != 0:
                cant = c
            c = (a + b) / 2
            erri = relerr(c, cant)
            if f(c) == 0:
                return c
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            i = i + 1
        return c


def relerr(vn, vl):
    """
    Función que calcula el error relativo.
    :param vn: Valor actual.
    :param vl: Valor anterior.
    :return: Error relativo en base a los dos valores.
    """
    return abs((vn-vl)/vn)
