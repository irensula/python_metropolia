# from the video

# class House():
#     '''description of the house'''
#     def __init__(self, street, number):
#         '''street and number of the house'''
#         self.street = street
#         self.number = number
#         self.age = 0
#     def build(self):
#         '''method which builds the house'''
#         print('The house on the street ' + self.street + ' with number ' + str(self.number) + ' is built.')
#     def age_of_house(self, year):
#         '''the age of the house'''
#         self.age += year

# House1 = House('Kyivska', 11)
# House2 = House('Kyivska', 12)

# print(House1.street)
# print(House2.number)

# House1.build()

# print(House1.age)

# House1.age_of_house(5)
# print(House1.age)

# class ProspectHouse(House):
#     '''houses on the prospect'''
#     def __init__(self, prospect, number):
#         super().__init__(self, number)
#         self.prospect = prospect

# PrHouse = ProspectHouse('Nauky', 5)
# print(PrHouse.prospect)


# 3. Luokan muodostaminen

# class Kytkin:
#     '''Kytkinluokka, joka sisältää Boolean-arvon.'''
#     __asento = False

#     def palauta(self):
#         return self.__asento
#     def muuta(self):
#         if self.__asento == False:
#             self.__asento = True
#         else:
#             self.__asento = False

# Lamppu = Kytkin()
# Lamppu.palauta() // False
# Lamppu.muuta()
# Lamppu.palauta // True


# 4. Jäsenmuuttujat

# class Asiakas:
#     nimi = 'Matti Meikäläinen'
#     loppusumma = 0
#     maksutapa = 'Luottokortti'
#     viitenumero = '1234-5678-9012345'
#     def tiedot(self):
#         print('Nimi:',self.nimi)
#         print('Loppusumma:',self.loppusumma)
#         print('Maksutapa:',self.maksutapa,end = ' ')
#         print('Viitenumero:',self.viitenumero)

# class Esimerkki:
#     pass
# Olio = Esimerkki()
# Olio.Arvo = 'Vapaamuotoinen muuttuja'
# print(Olio.Arvo)

# class toimitus:
#     '''Luokka määrittelee toimitettavat esineet'''
#     nimi = ''
#     osoite = ''

# def lisaa():
#     asiakas = input('Asiakkaan nimi: ')
#     paikka = input('Anna toimitusosoite: ')
#     paketti = toimitus()
#     paketti.nimi = asiakas
#     paketti.osoite = paikka

#     return paketti

# def main():
#     kierros = []
#     maara = int(input('Kuinka monta toimitusta?: '))
#     for i in range(0, maara):
#         toimitus = lisaa()
#         kierros.append(toimitus)
#     print('Vierailtavat paikat: ')

#     for i in range(0, maara):
#         print(kierros[i].nimi + ':' + kierros[i].osoite)

# if __name__ == "__main__":
#     main()


# class asiakas:
#     '''Luokka määrittelee toimitettavat esineet'''
#     kori = []
#     def lisaa(self):
#         esine = input('Mitä laitetaan koriin?: ')
#         self.kori.append(esine)

#     def kassalle(self):
#         print('Korissa oli seuraavat esineet: ')
#         for i in range(0,len(self.kori)):
#             print(self.kori[i], end = ' ')

# def main():
#     henkilo = asiakas()
#     while True:
#         valinta = input('Lisätäänkö tuote vai mennäänkö kassalle?: ')
#         if valinta == 'kassalle':
#             henkilo.kassalle()
#             break
#         else:
#             henkilo.lisaa()
# if __name__ == "__main__":
#     main() 


# class Kilpailija:
#     pisteet = 0
#     vari = []
    
# def eka():
#     ilmoitus = Kilpailija()
#     ilmoitus.vari = 'sininen'
#     ilmoitus.pisteet = 10
#     return ilmoitus

# def main():
#     Kilpailija = eka()
    
#     print('Kilpailijalla',ilmoitus.vari,'on',ilmoitus.pisteet,'pistettä!')



