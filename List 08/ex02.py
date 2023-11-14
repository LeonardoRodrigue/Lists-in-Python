dados = [1 ,2, 3, 4, 5, 6]
n1= n2 = n3 = n4 = n5 = n6 = 0

for i in range(10):

    dado = int(input("Jogue o dado e digite o valor que caiu: "))

    if(dado >= 1 and dado <= 6):
        dados.append(dado)
    else:
        print("Digite um valor valido, de 1 a 6!\n")
        continue
    
    if(dado == dados[0]):
        n1 += 1
    elif(dado == dados[1]):
        n2 += 1
    elif(dado == dados[2]):
        n3 += 1
    elif(dado == dados[3]):
        n4 += 1
    elif(dado == dados[4]):
        n5 += 1
    elif(dado == dados[5]):
        n6 += 1

print("O numero 1 foi repetido ", n1, " vezes.")
print("O numero 2 foi repetido ", n2, " vezes.")
print("O numero 3 foi repetido ", n3, " vezes.")
print("O numero 4 foi repetido ", n4, " vezes.")
print("O numero 5 foi repetido ", n5, " vezes.")
print("O numero 6 foi repetido ", n6, " vezes.")