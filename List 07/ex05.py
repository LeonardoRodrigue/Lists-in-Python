altura = []
idade = []
count =  0
soma_alts = 0
total_aluns = 0


for l in range(30):

    id = int(input("Digite a idade: "))
    idade.append(id)
    alt = float(input("Digite a altura: "))
    altura.append(alt)
    
for i in range(30):
    if idade[i] > 13:
        soma_alts += altura[i]
        total_aluns += 1

media_alt = soma_alts / total_aluns

for a in range(30):
    if idade[i] > 13 and altura[i] < media_alt:
        count += 1
print(count)

#Leonardo Rodrigues Reis Lopes