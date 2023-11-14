temperaturas = []
meses = [
    "1 - Janeiro",
    "2 - Fevereiro",
    "3 - Março",
    "4 - Abril",
    "5 - Maio",
    "6 - Junho",
    "7 - Julho",
    "8 - Agosto",
    "9 - Setembro",
    "10 - Outubro",
    "11 - Novembro",
    "12 - Dezembro"
]
soma_temps = 0

for mes in meses:
    temp = float(input(f"Digite a temperatura média do mês {mes}: "))
    temperaturas.append(temp)

for i in range(12):
    soma_temps += temperaturas[i]

media_temps = soma_temps / 12

for i in range(12):
    if temperaturas[i] > media_temps:
        print(f"{meses[i]} - {temperaturas[i]}ºC")

#Leonardo Rodrigues Reis Lopes