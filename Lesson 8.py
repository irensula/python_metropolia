# 1. Tiedoston käyttämimen
# tiedosto = open("text.txt","r")


# 2. Tiedoston lukeminen .read, .readline and .readlines
# tiedosto = open("text.txt","r")
# sisalto = tiedosto.readlines()

# print(sisalto)
# for i in sisalto:
#     print(i)

# tiedosto.close()


# 3. Tiedoston lukeminen esimerkki
# kahva = open('text.txt', 'r')
# teksti = kahva.read()
# print(teksti)
# kahva.close()


# 4. Tiedostojen käsittely ja sulkeminen
# def luejapalauta(nimi):
#     try:
#         tiedosto = open(nimi, 'r')
#         sisus = tiedosto.read()
#         tiedosto.close()
#         return sisus
#     except IOError:
#         return False

#####################################################

# tiedosto = open('text.txt', 'r')

# sisus = tiedosto.readline()
# sijainti = tiedosto.tell()
# print(sisus[:-1]+"; osoittimen sijainti on nyt", sijainti)

# print("Palataan merkkiin nro 10:")
# tiedosto.seek(10)
# sisus = tiedosto.read()
# print(sisus)

# tiedosto.close()


# 5. Lukuarvon käyttämisestä tiedosta

# luku = 1024

# tiedosto = open('lukutiedosto.txt', 'w')
# tiedosto.write(str(luku))
# tiedosto.close()

# luettu_luku = 0
# tiedosto = open('lukutiedosto.txt', 'r')
# luettu_luku = int(tiedosto.readline())
# tiedosto.close()

# print('Luettiin', luettu_luku, 'joka on muunnettiin numeroksi: ')
# luettu_luku = luettu_luku * 2
# print(luettu_luku)

# 6. Tiedoston kirjoittaminen

# def listapura(lista):
#     jono = ''
#     for i in range(0, len(lista)):
#         jono = jono + str(lista[i])
#     return jono

##########################################################

# tiedosto = open('kirjoitus.txt', 'w')

# teksti = 'Ensimmäinen rivi.\nToinen rivi.\nViimeinen rivi.'
# print(teksti)

# tiedosto.write(teksti)
# tiedosto.close()


# 7. Kirjoituksen jatkaminen

# tiedosto = open('kirjoitus.txt', 'a')

# lisays = 'Lisätty rivi!\nTiedostoa jatkettu edellisestä esimerkistä.\n'

# print(lisays)

# tiedosto.write(lisays)
# tiedosto.close()


# Tehtävä 1. Tiedoston kirjoittaminen
# tiedoston_nimi = input('Minkäniminen tiedosto luodaan?: ')
# file = open(tiedoston_nimi, 'a')
# kirjoitus = input('Mitä kirjoitetaan tiedostoon?: ')
# file.write(kirjoitus)
# print('Luotiin tiedosto',tiedoston_nimi,'ja siihen tallennettiin teksti:',kirjoitus)
# file.close()

# Tehtävä 2. Luetun datan seulonta, muuttujannimet

# file = open("merkkijonoja.txt","r")

# all_lines = file.readlines()

# for line in all_lines:
#     line_without_enter = line[:-1]
#     new_line = line_without_enter.isalnum()
#     if (new_line == True):
#         print(line_without_enter,'kelpaa salasanaksi.')
#     else:
#         print(line_without_enter,'sisältää virheellisiä merkkejä.')
# file.close()





# Tehtävä 3. Muistikirja: Kirjoita ja lue muistikirjaa

first_question = '''
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
'''

jatku = True

while jatku:
    print(first_question)
    valinta = int(input('Mitä haluat tehdä?: '))
    
    
    if(valinta == 1):
        file = open('muistio.txt', 'r')
        print(file.read())
        file.close()
        
         
    elif(valinta == 2):
        new_task1 = input('Kirjoita uusi merkintä: ')
        file = open('muistio.txt', 'a')
        # file.seek(0)
        # data = file.read(100)
        # if len(data) > 0 :
        file.write('\n')
        file.write(str(new_task1))
        file.close()

    elif(valinta == 3):
        open("muistio.txt", "w").close()
        print('Muistio tyhjennetty.')
    
    elif(valinta == 4):
        print('Lopetetaan.')
        break
    
    else:
        print("Invalid command. Enter 'help' for a list of available commands.")
        break