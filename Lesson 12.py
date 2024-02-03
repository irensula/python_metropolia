# .append, .insert, .remove, .pop, .index, .count, .sort(), .reverse()

# lista_1 = []
# lista_1.append('alkio')
# print(lista_1)
# lista_1.append(123123)
# print(lista_1)
# lista_1.remove('alkio')
# print(lista_1)

# lista_2 = ["Alkio", "Toinen", "Kolmas"]
# lista_2.pop(1)
# print(lista_2)

# lista_3 = ["Omenat","Maito","Olutta","Turtana"]
# print(lista_3)
# lista_3.append('Ananas')
# print(lista_3)
# lista_3.pop(1)
# print(lista_3)

# for i in lista_3:
#     print(i)

# lista_4 = [1,2,3,4,5,6,7,8]
# print(lista_4[2:5])
# print(lista_4[:6])
# print(lista_4[::-1])
# print(lista_4[3])

# lista_5 = ["Lapio", "Leka", "Pora", "Leka"]
# print(lista_5.index('Pora'))
# print(lista_5.count('Leka'))
# # print(lista_5.index('Vasara'))

# lista_6 = [1,2,3,4]
# for i in lista_6:
#     print(i)

# uusilista = []
# for i in lista_6:
#     uusilista.append(i+10)
# print(uusilista)

# Sanakirja (dictionary)
# def morsetus(sana):
#     aakkoset = {
#         'a' : '.-', 'b' : '-...',
#         'c' : '-.-.', 'd' : '-..',
#         'e' : '.', 'f' : '..-.',
#         'g' : '--.', 'h' : '....',
#         'i' : '..', 'j' : '.---',
#         'k' : '-.-', 'l' : '.-..'
#     }

#     kaannos = ""

#     for i in range(0, len(sana)):
#         kaannos = kaannos + aakkoset[sana[i]] + "/"
#     print('Sana',sana,'on morsekoodina')
#     print(kaannos)

# sana_1 = 'lakki'
# sana_2 = 'elegia'
# morsetus(sana_1)
# morsetus(sana_2)

# Tuple
# muuttuja1 = 'Auto'
# muuttuja2 = 'Kivikko'
# muuttuja3 = 'Sininen'
# tuplelista = muuttuja1,muuttuja2,muuttuja3
# print(tuplelista)

# def tulostus(tiedot):
#     osa1, osa2, osa3 = tiedot
#     print(osa1 + ":")
#     print(osa2 + "::" + osa3)

# nimi = "Juhani Turpea"
# osoite = "Kivipelto 10, 99999 Korvatunturi"
# puhelin = '555-1234567'

# tuplelista = (nimi, osoite, puhelin)

# tulostus(tuplelista) 

# Pickle-moduuli

# import pickle
# lista = ['Ananas', 'Karttakirja', ('Varsi', 'Tera'), 1150]
# tiedosto = open('tallenne.dat', 'wb')
# print(lista)
# pickle.dump(lista,tiedosto)
# tiedosto.close()

# Bittimuotoisen tiedon lukeminen

# import pickle
    # tiedosto = open('tallenne.dat', 'rb')
    # luettu = pickle.load(tiedosto)
    # print('Luettiin tallenne: ',luettu)
    # print(luettu[2], luettu[3])
    # tiedosto.close()

# Tehtävä 1

# lista = ["Sininen", "Punainen", "Keltainen", "Vihreä"]
# ens_alkio = lista[0]
# print('Listan ensimmäinen alkio on:',ens_alkio)
# print('Lista tulostettuna alkio kerrallaan:')
# for i in lista:
#     print(i)


# Tehtävä 2


# lista = []
 
# while(True):
#     syote = input('''
# Haluatko
# (1)Lisätä listaan
# (2)Poistaa listalta vai 
# (3)Lopettaa?: 
# ''')
#     valinta = int(syote)
#     if(valinta == 3):
#         print('Listalla oli tuotteet:')
#         for i in lista:
#             print(i)
#         break
#     elif(valinta == 1):
#         syote_1 = input('Mitä lisätään?: ')
#         lista.append(str(syote_1))
#     elif(valinta == 2):
#         try:
#             print('Listalla on',len(lista),'alkiota.')
#             syote_2 = input('Monesko niistä poistetaan?: ')
#             valinta_2 = int(syote_2)
#             lista.pop(valinta_2)
#         except IndexError:
#             print('Virheellinen valinta.')
#     else:
#         print('Virheellinen valinta.')


# Tehtävä 3

# lista = []
# tiedosto = open('sanoja.txt', 'r')
# tiedosto_read = tiedosto.read()

# tiedosto_split = tiedosto_read.replace('\n', ' ').split()

# tiedosto_split.sort()

# print('Sanat laitettuna aakkosjärjestykseen:')
# for sana in tiedosto_split:
#     print(sana)

# tiedosto.close()


# Tehtävä 4

import pickle
import time
def main():
    
    aikaleima = time.strftime("%X %x")
    lista = []
    try:
        tiedosto = open("muistio.dat", "rb")
        tiedosto.close()
    except FileNotFoundError:
        print('Virhe tiedostossa, luodaan uusi muistio.dat.')

    jatku = True
    while jatku:
        print('''
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta
''')
        valinta = int(input('Mitä haluat tehdä?: '))

        if(valinta == 2):
            tiedosto = open("muistio.dat", "wb")
            uusi_merkinta = input('Kirjoita uusi merkintä: ')
            lista.append(str(uusi_merkinta) + ':::' + aikaleima)
            pickle.dump(lista,tiedosto)
            tiedosto.close()

        elif(valinta == 3):
            tiedosto = open("muistio.dat","rb")
            lista = pickle.load(tiedosto)
            print('Listalla on',len(lista),'merkintää.')
            tiedosto.close()

            muutetaan = input('Mitä niistä muutetaan?: ')
            muutetaan_int = (int(muutetaan) - 1)
            print(lista[muutetaan_int])
            uusi_teksti = input('Anna uusi teksti: ')
            tiedosto = open("muistio.dat", "wb")
            lista[muutetaan_int] = str(uusi_teksti + ':::' + aikaleima)
            pickle.dump(lista,tiedosto)
            tiedosto.close()
        
        elif(valinta == 4):
            tiedosto = open("muistio.dat","rb")
            lista = pickle.load(tiedosto)
            print('Listalla on',len(lista),'merkintää.')
            tiedosto.close()

            tiedosto = open("muistio.dat", "wb")
            poistetaan = input('Mitä niistä poistetaan?: ')
            poistetaan_int = (int(poistetaan) - 1)
            poistettu = lista.pop(poistetaan_int)
            print("Poistettiin merkintä ",poistettu)
            pickle.dump(lista,tiedosto)
            tiedosto.close()

        elif(valinta == 1):
            tiedosto = open("muistio.dat","rb")
            lista = pickle.load(tiedosto)
            for i in lista:
                print(i)
            tiedosto.close()

        elif(valinta == 5):
            print('Lopetetaan.')
            break
if __name__ == '__main__':
    main()