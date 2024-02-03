# Moduulit

# import random
# luku = random.randint(0,100)
# print("Ohjelma arpoi luvun",luku)
# help(random.randint)

# write this commands in terminal
# import math
# dir(math)


# sys - exits the program
# import sys

# hinta = int(input('SYötä tuotteen hinta: '))
# if hinta < 0:
#     print('Ei negatiivisia lukuja.')
#     sys.exit(0)
# else:
#     vero = int(input('Syötä ALV-prosentti (0-100): '))
# if vero < 0:
#     print('Veroprosentti ei voi olla alle 0.')
#     sys.exit(0)
# print('Lopullinen hinta on',hinta*(vero/100)+hinta)


# import math
# sivu_1 = 1.5
# sivu_2 = 3.5

# print(math.sin(1.5 / 3.5))
# print(math.pi)

# import random
# numerot = []

# while True:
#     if len(numerot) == 7:
#         break
#     luku = random.randint(1,39)
#     if luku not in numerot:
#         numerot.append(luku)

# print('Ohjelma arpoi seuraavat luvut: ')
# numerot.sort()

# for i in numerot:
#     print(i, end=' ')

# from random import randint
# import sys

# def lukupeli():
#     luku = randint(0,100)
#     while True:
#         syote = int(input('Anna luku 0-100 väliltä: '))
#         if syote < 0:
#             print('Virheellinen syöte!')
#             sys.exit(0)
#         if syote == luku:
#             print('Arvasit oikein!')
#             break
#         elif syote < luku:
#             print('Luku on suurempi.')
#         else:
#             print('Luku on pienempi.')

# if __name__ == "__main__":
#     lukupeli()


# Tehtävä 1

# from random import randint

# def arpoo_viisi_kertaa():
#     print('Heitetään kolikkoa viidesti:')
#     i = 1
#     while i < 6:
    
#         luku = randint(0,1)
                
#         if luku == 0:
#             print('Klaava!')
#         elif luku == 1:
#             print('Kruuna!')
#         i += 1

# if __name__ == "__main__":
#     arpoo_viisi_kertaa()

# Tehtävä 2 *******************************

import moduuli

moduuli.tulosta("Esimerkkirivi")





# Tehtävä 3

# import tarkastaja
# while True:
#     testattava = input("Anna testattava sana: ")
#     tulos = tarkastaja.testaa(testattava)
#     if tulos == True:
#         print("Antamasi sana kelpaa salasanaksi!")
#         break
#     else:
#         print("Sana ei kelpaa.")


# Tehtävä 4

# import math

# input_1 = input('Anna ensimmäinen luku: ')
# input_2 = input('Anna toinen luku: ')

# jatku = True

# while jatku:
    
#     print('''
#     (1) +
#     (2) -
#     (3) *
#     (4) /
#     (5)sin(luku1/luku2)
#     (6)cos(luku1/luku2)
#     (7)Vaihda luvut
#     (8)Lopeta
#     ''')
#     print('Valitut luvut:',input_1, input_2)
    
#     valinta = int(input('Tee valinta (1-8): '))


#     if(valinta == 1):
#         valinta_1 = int(input_1) + int(input_2)
#         print('Tulos on:',valinta_1)
#     elif(valinta == 2):
#         valinta_2 = int(input_1) - int(input_2)
#         print('Tulos on:',valinta_2)
#     elif(valinta == 3):
#         valinta_3 = int(input_1) * int(input_2)
#         print('Tulos on:',valinta_3)
#     elif(valinta == 4):
#         valinta_4 = int(input_1) / int(input_2)
#         print('Tulos on:',valinta_4)
#     elif(valinta == 5):
#         valinta_5 = math.sin(int(input_1) / int(input_2))
#         print('Tulos on:',valinta_5)
#     elif(valinta == 6):
#         valinta_6 = math.cos(int(input_1) / int(input_2))
#         print('Tulos on:',valinta_6)
#     elif(valinta == 7):
#         input_1 = input('Anna uusi ensimmäinen luku: ')
#         input_2 = input('Anna uusi toinen luku: ')
#     elif(valinta == 8):
#         break

# Tehtävä 5

import time

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
        file.write('\n')
        file.write(str(new_task1))
        file.write(':::')
        file.write(time.strftime('%H:%M:%S, %d/%m/%Y'))
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