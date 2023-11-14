vetor = []

produto = 1

for i in range(5):
    num = int(input("Digite um numero inteiro: "))
    vetor.append(num)

for elemento in vetor:
    produto *= elemento

soma = sum(vetor)

print(f"A soma é {soma}")
print(f"A multiplicação é {produto}")