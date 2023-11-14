print('Em quantos anos o pais A passaria o pais B na quantidade de população?\nSe o pais A possui uma taxa de cre4scimento de 3%, ja o pais B possui de 1,5%? ')

popA = 80000
popB = 200000
anos = 0

while popA < popB:
    
    popA_com_acrec =  popA * 1.03
    popB_com_acrec =  popB * 1.015
    anos += 1

print('Seria de', anos, 'anos')

#Arthur Campibel e Leonardo Rodrigues