import numpy as np
import matplotlib.pyplot as plt

def falsa_posicao_x(a:float, b:float, e:float)->float|None:
    plot_grafico(a, b)
    if e < 1e-16:
        return None
    if f(a)*f(b) > 0:
        return None

    k = 1e10
    i = 0 
    
    while(k >= i):
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if f(a)*f(x) < 0:
            b = x
        elif f(b) * f(x) < 0:
            a = x
        i+=1

        
        if abs(b-a)<e :
            return x
    return x

def falsa_posicao_y(a:float, b:float, e:float)->float|None:
    plot_grafico(a, b)
    if e < 1e-16:
        return None
    if f(a)*f(b) > 0:
        return None

    k = 1e10
    i = 0 
    
    while(k >= i):
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if f(a)*f(x) < 0:
            b = x
        elif f(b) * f(x) < 0:
            a = x
        i+=1
        if abs(f(b)-f(a))<e :
            return x
    return x

def f(x:float) -> float:
    return np.sqrt(x) + np.exp(x) - 5

def plot_grafico(a:float, b:float, pace = 0.1) ->None:
    X = np.arange(a, b, pace)
    Y = np.array([f(x) for x in X])
    plt.plot(X,Y, color="blue")
    plt.show()

print(falsa_posicao_x(1,2,1e-6))