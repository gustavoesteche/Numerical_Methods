def soma_iterativa(x:float, epoch:int)->float:
    '''Realiza a soma iterativamente usando x:número a ser somado
    epoch: quantidade de vezes que se soma
    '''

    sum  = 0
    for i in range(epoch):
        sum += x
    return sum

def error(analitical_data:float, numerical_data:float)->tuple[float, float]:
    '''Calcula o erro absoluto e o erro relativo '''

    abs_error = abs(analitical_data - numerical_data)
    relative_error = abs(analitical_data - numerical_data)/analitical_data * 100
    
    return abs_error, relative_error

def get_result(x:float , epoch:int, analitical_data:float)->None:
    '''Printa o valor da soma, e os erros'''

    result = soma_iterativa(x, epoch)
    abs_error, relative_error = error(analitical_data, result)
    output = "Resultado: {} Erro absoluto: {} Erro relativo {}".format(result,abs_error,relative_error)
    print(output)


# aplica o algoritmo para os dois casos da questão
get_result(0.5, 30000, 15000)
get_result(0.11,30000,3300)