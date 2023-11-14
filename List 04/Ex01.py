while True:
    nota = float(input('Digite uma nota entre 0 e 10: '))

    if nota >= 0 and nota <= 10:
        print('Nota válida')
        break
    else:
        print('Nota inválida, digite novamente.')

#Arthur Campibel e Leonardo Rodrigues