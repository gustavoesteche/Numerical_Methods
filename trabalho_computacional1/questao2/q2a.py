import numpy as np
import time
from q2 import newton_method, f, analitical_derivative

# item (a)

# Aplica o método de newton, calcula o x, f(x), e calcula o tempo.

start = time.time()
result_newton = newton_method(1e-4, 1e-4, 0.5)
end = time.time()
print("tempo total: ", end - start)
print("Resultado para método de newton-raphson", result_newton)
print("Resultado de f(x)",f(result_newton),"\n")

# código para extrair cada aplicação da iteração 

def newton_method_iterations(e1:float, e2:float, x0:float):
    '''Realiza o método de newton-raphson para encontrar as raízes
    da função f(x) e printa o número de iterações.
    '''

    print("### método de newton valor a cada iteração ###")
    print("valor inicial de x =", x0)

    x1 = x0
    i = 1
    x2 = x0 - f(x0) / analitical_derivative(x0)
    print("\n # {}° iteração x = {} , f(x) = {}".format(i, x2, f(x2)))

    while((abs(f(x2)) > e1) or (abs((x2-x1)/x2) > e2)):
        i += 1
        x1 = x2
        x2 = x2 - f(x2) / analitical_derivative(x2)
        print("\n # {}° iteração x = {} , f(x) = {}".format(i, x2, f(x2)))
    
    print("iterações: ",i)
    return float(x2)


result_newton = newton_method_iterations(1e-4, 1e-4, 0.5)