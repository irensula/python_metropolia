# vari = input('Kerro lempivärisi: ')

# if vari == 'Sininen':
#     print('Sininen on erittäin hieno väri.')

# elif vari == 'Punainen':
#     print('Punainen sopii urheiluautoihin.')

# elif vari == 'Oranssi':
#     print('Oranssi väri tuo mieleen auringonlaskun.')

# else:
#     print(vari, 'on myös kaunis väri.')

# print('Tämä tulostusrivi on if-lauseen jälkeen ja suoritetaan aina.')

# and, or, not
# arvo_1 = 10
# arvo_2 = 'Hiukkanen'
# arvo_3 = 'Kivijalka'
# if (arvo_1 == 10) and (arvo_2 == 'Hiukkanen') and (arvo_3 == 5):
#     print('Toimii!')
# else:
#     print('Ei toiminut!')

# Tehtävä 1
# luku = input('Anna luku:')
# if (int(luku) % 2 == 0):
#     print('Antamasi luku oli parillinen.')

# Tehtävä 2

# nimi = input('Anna nimi: ')
# if(nimi != 'Erkki'):
#     print('Nimi oli väärin.')
# else:

#     salasana = input('Anna salasana: ')
#     if(salasana != 'Esimerkki'):
#         print('Salasana oli väärin.')
#     else:
#         print('Salasana ja nimi oli oikein!')

# Tehtävä 3

# kohde = input('Valitse kohde (1-3): ')
# if (int(kohde) == 1):
#     print("Haukion kala Oy")
# elif (int(kohde) == 2):
#     print('Metallipaja VasaraAika')
# elif (int(kohde) == 3):
#     print("Balin palapelitehdas")

# Tehtävä 4

# luku_1 = input('Anna luku: ')
# luku_2 = input('Anna toinen luku: ')
# if((int(luku_1) % 2 != 0) and (int(luku_2) % 2 != 0)):
#     print('Molemmat luvut ovat parittomia.')
# elif((int(luku_1) % 2 == 0) and (int(luku_2) % 2 == 0)):
#     print('Molemmat luvut ovat parillisia.')
# elif((int(luku_1) % 2 == 0) or (int(luku_2) % 2 == 0)):
#     print('Toinen luku on parillinen.')

# Tehtävä 5

input_1 = input('Anna ensimmäinen luku: ')
input_2 = input('Anna toinen luku: ')

print('''(1) +
(2) -
(3) *
(4) /''')

valinta = input('Tee valinta (1-4): ')
if(int(valinta) == 1):
    valinta_1 = int(input_1) + int(input_2)
    print('Tulos on:',valinta_1)
elif(int(valinta) == 2):
    valinta_2 = int(input_1) - int(input_2)
    print('Tulos on:',valinta_2)
elif(int(valinta) == 3):
    valinta_3 = int(input_1) * int(input_2)
    print('Tulos on:',valinta_3)
elif(int(valinta) == 4):
    valinta_4 = int(input_1) / int(input_2)
    print('Tulos on:',valinta_4)
else:
    print('Valintaa ei tunnistettu.')
