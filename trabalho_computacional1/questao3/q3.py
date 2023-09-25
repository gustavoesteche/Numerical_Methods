import numpy as np

# item (a)

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


def gauss_method(A:list[list], b:list[float])->tuple[list[list], list[float]] | None:
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
    
    # eliminação de gauss
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


# item (b)

def hilbert_matrix(n:int)->list[list]:
    '''função que retorna uma matriz de hilbert de dimensão n'''
    H = [[0] * n for i in range(n)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            H[i-1][j-1] = 1/(i+j-1)
    
    return H

def b_n(n:int)->list[float]:
    '''Função que monta e retorna a matriz pedida pela questão'''
    B = [0  for i in range(n)]

    for i in  range(1,n+1):
        for j in range(1,n+1):
            B[i-1] += 1/(i+j-1)

    return B

# item (c)

def norma_infinita(x:list[float]):
    '''Encontra e retorna a norma infinita de um vetor X'''
    max = abs(x[0])

    for i in range(1,len(x)):
        if abs(x[i]) > max:
            max = abs(x[i])
    
    return max


def gauss_jacobi(A:list[list], b:list[float], e:float, X:list[float], max_iterations:int):
    '''Aplica o método de gauss-jacobi para a resulção de sistemas lineares AX=b,
    e seu critério de parada se baseia na norma infinita da matriz solução
    '''
    
    m, n = len(A) , len(A[0])
    
    G = [[0] * n for i in range(m)]

    for i in range(m):
        for j in range(n):
            if i != j:
                G[i][j] = - A[i][j] / A[i][i]
            else:
                G[i][j] = 0
    
    
    c = b.copy()
    for i in range(m):
        c[i] = b[i] / A[i][i]

    G = np.array(G)
    c = np.array(c)
    X = np.array(X)
    
    X1 = np.dot(G,X) + c
    

    while(max_iterations >0):

        X = X1.copy()
        X1 = np.dot(G,X) + c
        max_iterations -= 1
        
        if max_iterations % 2 == 0:
            if(norma_infinita(X1 - X)/norma_infinita(X1) < e):
                break
        
    return X1