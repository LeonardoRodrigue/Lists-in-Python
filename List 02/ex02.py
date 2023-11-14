altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

area = altura * largura
quan_d_tinta = area / 3

print('Será nescessario {:.2f} de litros de tinta para pintar a sua parede de {:.1f} metros quadrados'. format(quan_d_tinta, area))

#Arthur Campibel e Leonardo Rodrigues