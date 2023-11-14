import random

numeros_digitados = []
numero = int(input("Digite um numeros aleatorios: "))

while True:
    if numero == 0:
        break
    else:
        numero = int(input("Digite um numeros aleatorios: "))
        numeros_digitados.append(numero)

maior_numero = max(numeros_digitados)

print('O maior numero é o:',maior_numero)

#Arthur Campibel e Leonardo Rodrigues