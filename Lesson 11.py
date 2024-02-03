# def otaluku():
#     luku = input('Anna lukuarvo: ')
#     return luku

# def main():
#     luku1 = otaluku()
#     luku2 = otaluku()
#     try:
#         tulos = int(luku1) / int(luku2)

#     except ZeroDivisionError:
#         print('Nollalla ei voi jakaa.')

#     except (TypeError, ValueError):
#         print('Kirjaimilla ei voi lskea.')

#     else:
#         print('Tulos on',tulos)

# if __name__ == "__main__":
#     main()

# else-osio
# luku = input('Anna lukuarvo: ')
# try:
#     luku = int(luku)
# except Exception:
#     print('Annoit virheellisen syötteen.')
# else:
#     print('Annoit luvun',luku)

# try-finally !!!!!!!!!!!!!!!

# luku = input("Anna lukuarvo: ")

# try:
#     luku = int(luku)
#     print("Annoit luvun",luku)

# finally:
#     print("Ohjelmassa oli virhe, lopetetaan.")


# Tehtävä 1

# luku = input('Anna luku: ')

# try:
#     luku = int(luku)
#     print('Syöte oli kelvollinen.')
# except Exception:
#     print('Virheellinen syöte!')


# Tehtävä 2

# tiedoston_nimi = input('Anna tiedoston nimi: ')

# try:
#     tiedosto = open(tiedoston_nimi,"r")
#     sisalto = int(tiedosto.readline())
#     tulos = sisalto + 313
#     print('Saatiin tulos ',tulos)
#     tiedosto.close()
# except IOError:
#     print('Virheellinen tiedostonnimi')
# except (ValueError):
#     print('Tiedoston sisältö virheellinen!')


# Tehtävä 3

# def pyyda_luku(prompt):
#     while True:
#         try:
#             luku = int(input(prompt))
#             return luku
#         except ValueError:
#             print("Virheellinen syöte!")

# import math

# def main():
#     luku_1 = pyyda_luku("Anna luku: ")
#     luku_2 = pyyda_luku("Anna luku: ")

#     while True:
        
#         print('''
#         (1) +
#         (2) -
#         (3) *
#         (4) /
#         (5)sin(luku1/luku2)
#         (6)cos(luku1/luku2)
#         (7)Vaihda luvut
#         (8)Lopeta
#         ''')
#         print('Valitut luvut:',luku_1, luku_2)
        
#         valinta = int(input('Tee valinta (1-8): '))


#         if(valinta == 1):
#             valinta_1 = luku_1 + luku_2
#             print('Tulos on:',valinta_1)
#         elif(valinta == 2):
#             valinta_2 = luku_1 - luku_2
#             print('Tulos on:',valinta_2)
#         elif(valinta == 3):
#             valinta_3 = luku_1 * luku_2
#             print('Tulos on:',valinta_3)
#         elif(valinta == 4):
#             valinta_4 = luku_1 / luku_2
#             print('Tulos on:',valinta_4)
#         elif(valinta == 5):
#             valinta_5 = math.sin(luku_1 / luku_2)
#             print('Tulos on:',valinta_5)
#         elif(valinta == 6):
#             valinta_6 = math.cos(luku_1 / luku_2)
#             print('Tulos on:',valinta_6)
#         elif(valinta == 7):
#             luku_1 = pyyda_luku("Anna luku: ")
#             luku_2 = pyyda_luku("Anna luku: ")
#         elif(valinta == 8):
#             break
  
# if __name__ == '__main__':
#     main()

# Tehtävä 4

import time
def main():
    
    # aikaleima = time.strftime("%X %x")
    tiedoston_nimi = 'muistio.txt'
    
    
    try:
        tiedosto = open(tiedoston_nimi, "r")
        tiedosto.close()
    except FileNotFoundError:
        print('Oletusmuistioa ei löydy, luodaan tiedosto.')
        tiedosto = open(tiedoston_nimi, "a")

    jatku = True

    while jatku:
        print('Käytetään muistiota: ',tiedoston_nimi)
        print('''
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta
''')
        valinta = int(input('Mitä haluat tehdä?: '))
                
        if(valinta == 1):
            file = open(tiedoston_nimi, 'r')
            print(file.read())
            file.close()
                
        elif(valinta == 2):
            new_task1 = input('Kirjoita uusi merkintä: ')
            file = open(tiedoston_nimi, 'a')
            file.write('\n')
            file.write(str(new_task1))
            file.write(':::')
            file.write(time.strftime('%H:%M:%S %d/%m/%Y'))
            file.close()

        elif(valinta == 3):
            open("muistio.txt", "w").close()
            print('Muistio tyhjennetty.')
        
        elif(valinta == 4):
            tiedoston_nimi = input('Anna tiedoston nimi: ')
            try:
                tiedosto = open(tiedoston_nimi, "r")
                tiedosto.close()
            except FileNotFoundError:
                print('Tiedostoa ei löydy, luodaan tiedosto.')
                
                tiedosto = open(tiedoston_nimi, "a")

        elif(valinta == 5):
            print('Lopetetaan.')
            break
        
        else:
            print("Invalid command. Enter 'help' for a list of available commands.")
            break
if __name__ == "__main__":
    main()