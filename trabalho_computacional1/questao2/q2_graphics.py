import matplotlib.pyplot as plt
import numpy as np
from q2 import newton_method, secante, bissecao, f

result_newton = newton_method(1e-4, 1e-4, 0.5)
result_sec = secante(5e-4,5e-4,-1,0.8)
result_bis = bissecao(-1.2,4,1e-4,1e-4)

# plota o gráfico da função
X = np.arange(-4,4, 0.1)
Y = [f(x) for x in X]
plt.title("Gráfico da função de f(x) por x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(X,Y, c='blue', label = "f(x)")


# plota os pontos encontrados no gráfico, note que precisa dar 
# zoom para melhor vizualização.
plt.scatter([result_newton],[0],s=3 ,c='red', label ="Newton-Raphson")
plt.scatter([result_sec],[0],s = 3, c='green', marker="*", label = "Secante")
plt.scatter([result_bis],[0],s = 3, c='purple', marker="<", label = "Bisseção")
plt.legend(loc="lower right", fancybox=True)
plt.savefig("my_plot.png", format="png")
plt.show()