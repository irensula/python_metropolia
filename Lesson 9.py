# def omafunktio():
#     print('Tämä tulostus tulee alifunktiosta!')
# print('Tämä tulostus tulee pääfunktiosta!')

# omafunktio()
# omafunktio()

def Laskuri(luku_1, luku_2):
    """Ohjelma vastaanottaa kaksi lukuarvoa"""

    if luku_1 == luku_2:
        print('Luvut ovat yhtä suuria.')
    elif luku_1 > luku_2:
        print('Ensimmäinen luku on suurempi.')
    else:
        print('Toinen luku on suurempi.')
Laskuri(5,1)
arvo1 = 10
arvo2 = 5
Laskuri(arvo1, arvo2)

# def tulostusfunktio(sana_1, sana_2):
#     print('Annoit parametrit',sana_1,'ja',sana_2)

# def main():
#     merkkijono_1 = 'Hapankaalia'
#     merkkijono_2 = 'Silakoita'

#     tulostusfunktio(merkkijono_1, merkkijono_2)

# if __name__ == '__main__':
#     main()

# def testaa(merkkijono = ""):
#     if len(merkkijono) < 8:
#         return False
#     else:
#         return True

# def ota_sana():
#     syote = input("Syötä uusi salasana: ")
#     return syote

# def main():
#     while True:
#         ehdokas = ota_sana()
#         tulos = testaa(ehdokas)
#         if tulos == False:
#             print("Salasana on liian lyhyt.")
#             print("Yritä uudelleen.")
#         else:
#             print("Uusi salasana hyväksytty!")
#             print("Lopetetaan.")
#             break

# if __name__ == "__main__":
#     main()

# Lambda funktio
# def lisuri(n):
# 	return lambda summa: summa + n


# Tehtävä 1

# def main():
#     print('Tulostusfunktio!')
# if __name__ == '__main__':
#     main()


# Tehtävä 2
    
# def toinenpotenssi(lukuarvo):
#     vastaus = int(lukuarvo) * int(lukuarvo)
#     print('Toinen potenssi on',vastaus)

# def main():
#     luku = input('Anna lukuarvo: ')
#     toinenpotenssi(luku)

# if __name__ == '__main__':
#     main()


# Tehtävä 3

# def alifunktio(sana='Oletustulostus'):
#     print(sana)

# def main():
#     jatku = True
#     while(jatku):
#         syote = input('Anna syöte (Lopeta lopettaa): ')
#         if(syote == 'Lopeta'):
#             break
#         elif(len(syote) > 5):
#             alifunktio(syote)
            
#         elif(len(syote) < 5):
#             alifunktio()
    
# if __name__ == '__main__':
#     main()

# Tehtävä 4

# def alifunktio(sana):
#     sananpituus = len(sana)
#     return sananpituus


# def main():
#     jatku = True
#     while(jatku):
#         syote = input('Anna syöte (Lopeta lopettaa): ')
#         syotepituus = alifunktio(syote)
#         if(syote == 'Lopeta'):
#             break
#         elif(syotepituus >= 1):
#             print('Antamasi syöte oli',syotepituus,'merkkiä pitkä')
#         elif(syotepituus < 1):
#             print('Et antanut syötettä')
    
# if __name__ == '__main__':
#     main()



