perguntas = {'p1' : False, 'p2' : False, 'p3' : False, 'p4' : False, 'p5' : False}
pgTrue = []

p1 = input("Telefonou para a vitima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Mora perto da vitima? ")
p4 = input("Devie para a vitima? ")
p5 = input("Ja trabalhou com a vitima? ")

if (p1 == "sim" or p2 == "s"):
    perguntas['p1'] = True
elif (p2 == "sim" or p2 == "s"):
    perguntas['p2'] = True
elif (p3 == "sim" or p3 == "s"):
    perguntas['p3'] = True
elif (p4 == "sim" or p4 == "s"):
    perguntas['p4'] = True
elif (p5 == "sim" or p5 == "s"):
    perguntas['p5'] = True

