numeros_digitados = []
count = 0

while True:
    numero = int(input("Digite um numero para ser armazenado: "))

    if numero == -1:
        break
    else:
        numeros_digitados.append(numero)
        count += 1

soma = sum(numeros_digitados)
media = soma / len(numeros_digitados)
maior_que_a_media = [num for num in numeros_digitados if num > media]
menor_que_sete = [num for num in numeros_digitados if num < 7]


print(f"\nForam lidos {count} numeros...\n")

print(f"Na ordem são eles: {numeros_digitados}\n")

print("Em ordem inversa: ")
for numero in reversed(numeros_digitados):
    print(numero)

print(f"\nA soma dos numeros é: {soma}")
if maior_que_a_media:
    print("\nOs valores a cima da média são: ")
    for maiores in maior_que_a_media:
        print(maiores)
if menor_que_sete:
    print("\nOs numeros menor que 7 são: ")
    for menores in menor_que_sete:
        print(menores)

print("\nObrigado por usar o programa!")

#Leonardo Rodrigues Reis Lopes