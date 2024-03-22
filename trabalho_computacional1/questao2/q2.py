import numpy as np
import sympy as sp
import time
import matplotlib.pyplot as plt



# define a função que vai ser trabalhada no problema
def f(x):
    return x ** 3 - 9 * x + 3 
# adding a sill commment



# item (a)
def analitical_derivative(y:float):
    '''Calcula a expressão analítica da derivada da
    função f(x) usando a bliblioteca sympy.
    '''
    x = sp.symbols('x')
    expression = f(x)
    derivative = sp.diff(expression, x)

    return derivative.subs(x, y)


def newton_method(e1:float, e2:float, x0:float):
    '''Realiza o método de newton-raphson para encontrar as raízes
    da função f(x) e printa o número de iterações.
    '''

    print("### método de newton ###")

    x1 = x0
    i = 1
    x2 = x0 - f(x0) / analitical_derivative(x0)

    while((abs(f(x2)) > e1) or (abs((x2-x1)/x2) > e2)):
        i += 1
        x1 = x2
        x2 = x2 - f(x2) / analitical_derivative(x2)
    
    print("iterações: ",i)
    return float(x2)




# item (b)
def secante(e1:float, e2:float, x0:float, x1:float)->float:
    '''Realiza o método da secante para encontrar as
    raízes da função f(x)
    '''

    print("### método da secante ###")
    i = 1
    x2 = (x0*f(x1) - x1 *f(x0))/(f(x1) - f(x0))
    
    while((abs(f(x2)) > e1) or (abs((x2-x1)/x2) > e2)):
        i+=1
        temp = x2
        x2 = (x1*f(x2) - x2 *f(x1))/(f(x2) - f(x1))
        x1 = temp
    print("iterações: ",i)
    return x2 


# item (c)
def bissecao(x0:float, x1:float, e1:float, e2:float)->float:
    '''Realiza o método da bisseção para encontrar as raízes
    da função f(x)
    '''

    print("### método da bisseção ###")

    i = 0 
    x = (x0 + x1)/2
    previous_x = 0
    while ((abs(f(x)) > e1) or (abs(x - previous_x)/x > e2)):
        i+=1
        previous_x = x
        if f(x0)*f(x) < 0:
            x1 = x
        elif f(x1) * f(x) < 0:
            x0 = x
        x = (x0 + x1)/2
    print("iterações: ",i)
    return x
