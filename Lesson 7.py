# While-toistorakenne

# 1
# kierroksia = int(input('Kuinka monta kirrosta: '))
# kierros = 0

# while(kierros < kierroksia):
#     print('Nyt olemme kierroksella',kierros)
#     kierros += 1

# 2
# kierros = 0

# while kierros < 6:
#     print('Toistorakenne!')
#     if kierros == 5:
#         print('Vihdoin on loppu!')

#     kierros += 1

# 3
# kertoma = int(input('Minkä luvun kertoma lasketaan?: '))

# tulos = int(1)

# for kierros in range(1,kertoma+1):
#     tulos = tulos * kierros
#     print('Kierroksella',kierros,'tuolos on',str(tulos)+'.')

# print('Lopullinen vastaus on',tulos)

#4
# for i in range(5):
#     print(i)

#5
# for i in range(104,108):
#     print(i)

#6
# muuttuja = 3
# for i in range(muuttuja):
#     print(i)

#7
# jatkuu = True
# while jatkuu:
#     syote = input('Kirjoita jotain: ')

#     if syote == 'Lopeta':
#         jatkuu = False
#     else:
#         print(syote)

#8
# kierrosmaara = 0
# jatka = True
# while jatka: 
#     print('Toistorakenne!')
#     if kierrosmaara == 100:
#         jatka = False

#9
# kierrosmaara = 0
# jatka = True
# while jatka:
#     print('Toistorakenne!')
#     if kierrosmaara == 100:
#         print('Vihdoin on loppu!')
#         jatka = False
        
#     else:
#         kierrosmaara = kierrosmaara + 1

#10 break

# aloituspaikka = int(input('Aloituspaikka: '))
# while True:
#     if aloituspaikka % 13 == 0:
#         print('Löydettiin 13 jaollinen luku!')
#         break
#     else:
#         print('Olemme luvussa",aloituspaikka,"jatketaan...')
#         aloituspaikka += 1

#11 continue

# lukuja = 0
# summa = 0

# while True:
#     luku = int(input('Anna lukuarvo: '))

#     if luku == 0:
#         print('Ohitetaan 0.')
#         continue
#     elif luku < 0:
#         print('Summa on', summa)
#         print('Laskettiin yhteen',lukuja,'lukua.')
#         break
#     else:
#         lukuja = lukuja + 1
#         summa = summa + luku

#12 pass
# for i in range (0,10):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i, 'on pariton luku.')

#13 else

# alku = int(input('Anna aloituspaikka: '))
# loppu = int(input('Anna lopetuspaikka: '))

# lista = range(alku, loppu)

# for alkio in lista:
#     if alkio == 42:
#         print('Luku 42 löytyi listalta!')
#         break
#     else:
#         print('Haettua lukua ei löytynyt')

# Tehtävä 1
# kierros = 0
# kierroksia = 4
# while(kierros <= kierroksia):
#     print('Olemme kierroksella ',kierros)
#     kierros += 1

# Tehtävä 2
# jatku = True

# while jatku:
#     syote = input('Kirjoita jotain: ')

#     if syote == 'lopeta':
#         print('Lopetit ohjelman.')
#         jatku = False
#     else:
#         print(syote)

# Tehtävä 3

# kierrosmaara = int(input('Kuinka monta kierrosta?: '))
# tulos = 0
# for num in range(1, kierrosmaara):
#      tulos += num

# print('Kertymäksi saatiin:',tulos) 


# Tehtävä 4

input_1 = input('Anna ensimmäinen luku: ')
input_2 = input('Anna toinen luku: ')

jatku = True

while jatku:
    
    print('''
    (1) +
    (2) -
    (3) *
    (4) /
    (5)Vaihda luvut
    (6)Lopeta
    ''')
    print('Valitut luvut:',input_1, input_2)
    
    valinta = int(input('Tee valinta (1-6): '))


    if(valinta == 1):
        valinta_1 = int(input_1) + int(input_2)
        print('Tulos on:',valinta_1)
    elif(valinta == 2):
        valinta_2 = int(input_1) - int(input_2)
        print('Tulos on:',valinta_2)
    elif(valinta == 3):
        valinta_3 = int(input_1) * int(input_2)
        print('Tulos on:',valinta_3)
    elif(valinta == 4):
        valinta_4 = int(input_1) / int(input_2)
        print('Tulos on:',valinta_4)
    elif(valinta == 5):
        input_1 = input('Anna uusi ensimmäinen luku: ')
        input_2 = input('Anna uusi toinen luku: ')
    elif(valinta == 6):
        break
    
    else:
        print(input_1, input_2)