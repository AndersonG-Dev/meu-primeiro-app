def maior(numeros):
    maior_agora = numeros[0]
    for numero in numeros:
        if numero > maior_agora:
            maior_agora = numero
    return maior_agora

numeros = [3, 7, 1, 9, 5]
print(f"Maior numero entres os numeros {numeros} é {maior(numeros)}")
