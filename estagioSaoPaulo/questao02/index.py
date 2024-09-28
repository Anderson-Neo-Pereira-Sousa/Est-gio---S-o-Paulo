# Faz a sequencia de Fibonacci
def sequenciaFibonacci(num): 
    listaFib = [0, 1]
    while True:
        proximoFib = listaFib[-1] + listaFib[-2]
        if proximoFib > num:
            break
        listaFib.append(proximoFib)
    return listaFib


# Verifica se numero pertence a Fibonacci
def verificaFibonacci(num):
    if num < 0:
        return False
    listaFib = sequenciaFibonacci(num)
    return num in listaFib

# Entrada
num = 34

if verificaFibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")