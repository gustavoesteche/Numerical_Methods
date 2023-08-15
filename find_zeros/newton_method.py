import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def f(x):
    return x ** 3 - 2 * x ** 2 + 7 * x + 12 

def numerical_derivative(y:float):
    x = sp.symbols('x')
    expression = f(x)
    derivative = sp.diff(expression, x)
    return derivative.subs(x, y)

def newton_method(interations:int, x0:float):
    x = x0
    for i in range(interations):
        x = x - f(x) / numerical_derivative(x)
    return float(x)

print(newton_method(2,2))

X = np.arange(-2.5,2.5,0.1)
Y = f(X)

plt.plot(X, Y, color="red")
plt.show()