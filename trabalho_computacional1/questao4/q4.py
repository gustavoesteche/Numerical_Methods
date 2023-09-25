import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# item (a)
def norma_infinita(x:list[float]):
    '''Encontra e retorna a norma infinita de um vetor X'''
    max = abs(x[0])

    for i in range(1,len(x)):
        if abs(x[i]) > max:
            max = abs(x[i])
    
    return max

def partial_pivoting(A:list[list], b:list[float])->tuple[list[list], list[float]]:
    '''Realiza o pivoteamento parcial em uma matriz para que posteriormente seja
    aplicado o método de eliminação de Gauss'''

    for j in range(len(A[0])):
        max = A[j][j]
        max_l = j
        for i in range(j,len(A)):
            if A[i][j] > max:
                max = A[i][j]
                max_l = i
        temp = A[j]
        temp_ = b[j]

        A[j] =  A[max_l]
        b[j] = b[max_l]

        A[max_l] = temp
        b[max_l] = temp_

        
    return A, b


def gauss_method(A:list[list], b:list[float])-> list[float] | None:
    '''Aplica o método de eliminação de gauss para resolver o sistema linear Ax = b
    e retorna uma tupla com a forma reduzida de A, b, se A for a identidade, x = b
    '''
    A_reduzida = A.copy()
    b_reduzida = b.copy()

    A_reduzida, b_reduzida = partial_pivoting(A_reduzida, b_reduzida)
    if len(A) != len(b):
        return
    m = len(b)
    n = len(A[0])
    

    for i in range(n):
        for j in range(i + 1, m):
            multiplicador = A_reduzida[j][i] / A_reduzida[i][i]
            for k in range(n):
                A_reduzida[j][k] = A_reduzida[j][k] - multiplicador * A_reduzida[i][k]
            b_reduzida[j] = b_reduzida[j] - multiplicador * b_reduzida[i]

    # resolução do sistema triangular 
    x = [0] * m
    for i in range(n - 1, -1, -1):
        x[i] = b_reduzida[i] / A_reduzida[i][i]
        for j in range(i - 1, -1, -1):
            b_reduzida[j] -= A_reduzida[j][i] * x[i]

    return x 


def expression(x1:float, x2:float)->list[float]:
        '''Define as duas equações que têm-se como objetivo zerar-se simultâneamente
        utilizando o método de newton'''
        return np.array([4 * x1 - x1 ** 3 + x2, -(x1 ** 2)/9 + x2 -(x2**2)/4 + 1])

def jacobian(x1:float, x2:float)->list[list]:
    '''Define a expressão da Jacobiana da função matricial que queremos zerar'''
    return np.array([[4 - 3* x1 ** 2, 1],[-2/9 * x1, 1 - 0.5 * x2]])


def Newton_Method_2var(x1:float, x2:float, max:int , error_f:float, error_X:float) -> tuple[float, float]:
    '''Realiza o método de newton para o sistema de duas variáveis'''
    x_k = np.array([x1,x2])
    x = np.array([x1,x2])

    while(max):
        x_k = x
        if(norma_infinita(expression(x_k[0], x_k[1])) < error_f):
            break
        
        J = jacobian(x_k[0], x_k[1])
        F = expression(x_k[0], x_k[1])

        x = gauss_method(J, -1 * F) + x_k

        if(norma_infinita(x - x_k) < error_X):
            break

        max -= 1

    return x

sol = Newton_Method_2var(0,0,100,0.001, 0.001)
print("solução da equação pelo método de newton")
print("solução  x1 = {} | x2 = {}".format(sol[0], sol[1]))
a, b = expression(sol[0], sol[1])
print("resultado da primeira função",a)
print("resultado da segunda função",b)
print("\n \n")


#item (b)

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

Z1, Z2 = expression(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1, cmap='hot')
ax.set_xlabel('x1 ')
ax.set_ylabel('x2 ')
ax.set_zlabel('F')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z2, cmap='cool')
ax.set_xlabel('x1 ')
ax.set_ylabel('x2 ')
ax.set_zlabel('F')
plt.show()



#item (c)

sol = Newton_Method_2var(0,0,100,1e-12 ,1e-12)
print("solução da equação pelo método de newton para o item b)")
print("solução  x1 = {} | x2 = {}".format(sol[0], sol[1]))
a, b = expression(sol[0], sol[1])
print("resultado da primeira função",a)
print("resultado da segunda função",b)
print("\n \n")


sol = Newton_Method_2var(0,0,100,1e-25, 1e-25)
print("solução da equação pelo método de newton para o item c)")
print("solução  x1 = {} | x2 = {}".format(sol[0], sol[1]))
a, b = expression(sol[0], sol[1])
print("resultado da primeira função",a)
print("resultado da segunda função",b)
print("\n \n")


