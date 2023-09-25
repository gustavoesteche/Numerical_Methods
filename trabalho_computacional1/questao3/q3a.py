from q3 import gauss_method

# sistema dado pela questão
A = [[2,2,1,1],[1,-1,2,-1],[3,2,-3,-2],[4,3,2,1]]
b = [7,1,4,12]

solucao  = gauss_method(A,b)
print("Solução do item (a) pelo método de gauss:")
print(solucao)
print("\n")
