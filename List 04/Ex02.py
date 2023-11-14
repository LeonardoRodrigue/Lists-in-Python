while True:
    nome = input('Digite um nome: ')

    if len(nome) >= 5 and len(nome) <=15:
        print('Nome válido!')
        break
    else:
        print('Nome inválido, tente novamente.')

#Arthur Campibel e Leonardo Rodrigues