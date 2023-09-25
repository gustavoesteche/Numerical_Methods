from q3 import gauss_jacobi, hilbert_matrix, b_n 

print("Solução do item (a) utilizando método de gauss-jacobi\n")

A = [[2,2,1,1],[1,-1,2,-1],[3,2,-3,-2],[4,3,2,1]]
b = [7,1,4,12]

sol = gauss_jacobi(A,b,0.01,[0,0,0,0],100)
print(sol, "\n")



print("Solução do item (b) utilizando método de gauss-jacobi\n")

casos = [4, 10, 20]
for n in casos:
    H = hilbert_matrix(n)
    b = b_n(n)
    X = [0 for i in range(n)]
    sol = gauss_jacobi(H,b,0.001, X, 100)
    print("dimensão da matriz n = {}: \n".format(n))
    print(sol)    
    print("\n")

'''
A_= [[10,2,1],[1,5,1],[2,3,10]]
b_ = [7,-8,6] 
sol1 = gauss_jacobi(A_,b_,0.001,[0,0,0],10)
print(sol1)
'''