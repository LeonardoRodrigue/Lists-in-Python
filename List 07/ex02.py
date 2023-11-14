list = []
impares = []
pares = []

for i in range(0,20):
    numbers = int(input("Digite 20 numeros:"))
    list.append(numbers)

    if numbers % 2 == 0:
        pares.append(numbers)
    else:
        impares.append(numbers)

print(list)
print(pares)
print(impares)

#Leonardo Rodrigues Reis Lopes