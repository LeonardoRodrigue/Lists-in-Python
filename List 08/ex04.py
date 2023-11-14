idade = []
altura = []

for i in range(5):
    ida = int(input("Digite a idade: "))
    idade.append(ida)
    alt = float(input("Digite a altura: "))
    altura.append(alt)

idade.reverse()
altura.reverse()

print(idade)
print(altura)