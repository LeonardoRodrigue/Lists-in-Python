listmedia = []
cont = 0

for i in range(0,10):

    nota1 = int(input("Digite a primeira nota:"))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a segunda nota: "))

    media = (nota1+nota2+nota3+nota4) / 4

    listmedia.append(media)

    if media >= 7:
        cont+=1

print(listmedia)
print(cont)

#Leonardo Rodrigues Reis Lopes
    
        