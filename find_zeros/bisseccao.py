import numpy as np
import matplotlib.pyplot as plt

def bisseccao_x(a:float, b:float, e:float)->float|None:
    plot_grafico(a, b)
    if e < 1e-16:
        return None
    if f(a)*f(b) > 0:
        return None

    k = np.log2(abs(b-a)/e)
    i = 0 
    
    while(k >= i):
        x = (a + b) / 2
        if f(a)*f(x) < 0:
            b = x
        elif f(b) * f(x) < 0:
            a = x
        i+=1
        if abs(b-a)<e :
            return x
    return None

def bisseccao_y(a:float, b:float, e:float)->float|None:
    plot_grafico(a, b)
    if e < 1e-16:
        return None
    if f(a)*f(b) > 0:
        return None

    k = np.log2(abs(b-a)/e)
    i = 0 
    
    while(k >= i):
        x = (a + b) / 2
        if f(a)*f(x) < 0:
            b = x
        elif f(b) * f(x) < 0:
            a = x
        i+=1

        if abs(f(b)-f(a))< e:
            return x
    
    return None


def f(x:float) -> float:
    return x ** 3 - 9 * x + 3 

def plot_grafico(a:float, b:float, pace = 0.1) ->None:
    X = np.arange(a, b, pace)
    Y = np.array([f(x) for x in X])
    plt.plot(X,Y, color="blue")
    plt.show()



