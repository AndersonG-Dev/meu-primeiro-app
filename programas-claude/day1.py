def pares(numeros):
    resultado = []
    for numero in numeros:
        if numero % 2 == 0:
            resultado.append(numero)
    return resultado  # mesma indentação do for
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(pares(numeros))
