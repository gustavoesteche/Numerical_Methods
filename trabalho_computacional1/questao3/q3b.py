from q3 import gauss_method, hilbert_matrix, b_n

def print_latex(x):
    for i in range(len(x)-1):
        print(x[i],"\\\\")
    print(x[len(x)-1])

print("Solução para o sistema com a matriz de hilbert com o método de gauss : \n")

casos = [4, 10, 20]
for n in casos:
    H = hilbert_matrix(n)
    b = b_n(n)
    sol = gauss_method(H,b)
    
    print("dimensão da matriz n = {}: \n".format(n))
    print(sol)
    print("\n")

