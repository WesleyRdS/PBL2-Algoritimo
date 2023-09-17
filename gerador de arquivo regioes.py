from random import randint

arquivo = open('exemploPesquis.txt','w',encoding= 'UTF-8')
for i in range(0,100):
    arquivo.write('T')
    arquivo.write(str(randint(1000,9999)))
    arquivo.write(';')
    x = randint(0,12)
    if x == 0:
        arquivo.write("Rio Branco")
    elif x == 1:
        arquivo.write("Cruzeiro do Sul")
    elif x == 2:
        arquivo.write("Macapá")
    elif x == 3:
        arquivo.write("Laranjal do Jari")
    elif x == 4:
        arquivo.write("Manaus")
    elif x == 5:
        arquivo.write("Manicoré")
    elif x == 6:
        arquivo.write("Belém")
    elif x == 7:
        arquivo.write("Macará")
    elif x == 8:
        arquivo.write("Porto Velho")
    elif x == 9:
        arquivo.write("Rolim de Moura")
    elif x == 10:
        arquivo.write("Boa Vista")
    elif x == 11:
        arquivo.write("Palmas")
    elif x == 12:
        arquivo.write("Porto Nacional")
    arquivo.write(';')
    arquivo.write(str(randint(3000000,4000000)))
    arquivo.write(';')
    if x == 0 or x == 1:
        arquivo.write("AC")
    elif x == 2 or x == 3:
        arquivo.write("AP")
    elif x == 4 or x == 5:
        arquivo.write("AM")
    elif x == 6 or x == 7:
        arquivo.write("PA")
    elif x == 8 or x == 9:
        arquivo.write("RO")
    elif x == 10:
        arquivo.write("RR")
    elif x == 11 or x == 12:
        arquivo.write("TO")
    arquivo.write(';')
    if x == 0 or x == 1:
        arquivo.write("Acre")
    elif x == 2 or x == 3:
        arquivo.write("Amapá")
    elif x == 4 or x == 5:
        arquivo.write("Amazonas")
    elif x == 6 or x == 7:
        arquivo.write("Pará")
    elif x == 8 or x == 9:
        arquivo.write("Rondônia")
    elif x == 10:
        arquivo.write("Roraima")
    elif x == 11 or x == 12:
        arquivo.write("Tocantins")
    arquivo.write(";")
    arquivo.write(str(randint(100,900)))
    arquivo.write('\n')