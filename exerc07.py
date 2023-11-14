n = int(input('Digite o numero para saber a sua tabuada: '))
numlimit = 10
multi = 0
while True:
    multi += 1
    result = n * multi
    
    print('{} x {} = {}'.format(n, multi , result))

    if multi == numlimit:
        break

#Arthur Campibel e Leonardo Rodrigues