import time
from q2 import bissecao, f

#item (c)

# Aplica o método da bisseção, calcula x, f(x) e o tempo

start = time.time()
result_bis = bissecao(-1.2,4,1e-4,1e-4)
end = time.time()
print("tempo total",end - start)
print("Resultado usando bisseção", result_bis)
print("Resultado de f(x)", f(result_bis))

def bissecao_iterations(x0:float, x1:float, e1:float, e2:float)->float:
    '''Realiza o método da bisseção para encontrar as raízes
    da função f(x)
    '''

    print("### método da bisseção ###")
    print("valores iniciais a = {} e b = {}".format(x0,x1))
    i = 1
    x = (x0 + x1)/2
    print("\n # {}° iteração x = {} , f(x) = {}".format(i, x, f(x)))
    previous_x = 0
    while ((abs(f(x)) > e1) or (abs(x - previous_x)/x > e2)):
        i+=1
        previous_x = x
        if f(x0)*f(x) < 0:
            x1 = x
        elif f(x1) * f(x) < 0:
            x0 = x
        x = (x0 + x1)/2
        print("\n # {}° iteração x = {} , f(x) = {}".format(i, x, f(x)))
    print("iterações: ",i)
    return x

result_bis = bissecao_iterations(-1.2,4,1e-4,1e-4)