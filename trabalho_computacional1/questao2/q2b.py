import numpy as np 
import time
from q2 import secante, f

#item (b)

# Aplica o método da secante, cálcula x, f(x) e o tempo.

start = time.time()
result_sec = secante(5e-4,5e-4,0,1)
end = time.time()
print("tempo total",end - start)
print("Resultado usando secante",result_sec)
print("Resultado de f(x)", f(result_sec), "\n")


# código para extrair cada aplicação da iteração 

def secante_iterations(e1:float, e2:float, x0:float, x1:float)->float:
    '''Realiza o método da secante para encontrar as
    raízes da função f(x)
    '''

    print("### método da secante para cada iteração ###")
    print("valor incial de x1 = {}, x2 = {}".format(x0, x1))


    i = 1
    x2 = (x0*f(x1) - x1 *f(x0))/(f(x1) - f(x0))
    print("\n # {}° iteração x1 = {}, x2 = {}, f(x) = {}".format(i,x1, x2, f(x2)))
    
    
    while((abs(f(x2)) > e1) or (abs((x2-x1)/x2) > e2)):
        i+=1
        temp = x2
        x2 = (x1*f(x2) - x2 *f(x1))/(f(x2) - f(x1))
        x1 = temp
        print("\n # {}° iteração x1 = {}, x2 = {}, f(x2) = {}".format(i,x1, x2, f(x2)))
    
    print("iterações: ",i)
    return x2 

result_sec = secante_iterations(5e-4,5e-4,0,1)

print("\n## resultado usando diferentes pontos iniciais ##\n")
result_sec1 = secante(5e-4,5e-4,-1,0.8)
print("Resultado usando secante",result_sec1)
print("Resultado de f(x)", f(result_sec1), "\n")
