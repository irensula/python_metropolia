muuttuja1 = 1000
muuttuja2 = 24
tulos = (muuttuja1 + muuttuja2 + 15) ** 2 
print("Laskutoimituksen tulos on: " + str(tulos))

print('Tekstitulostus!')
print('Toinen rivi!')

muuttuja = 4
print("Seinällä on", muuttuja, "valoa.")

# when we use , it adds spaces 
print("Sait arvosanan", muuttuja, "!")

# when we use + it doesn't add spaces
huudahdus = "Juoskaa"
print(huudahdus + "!")

# end="" adds two strings together with space between them
print("Esimerkkilause johon ei tule rivinvaihtoa. ", end="")
print("Tämä tulee heti perään.")

# sep='' takes out spaces between strings and variables
muuttuja = 4
print("Kvartetissa on", muuttuja, "jäsentä.", sep='')

print("Pääjohtaja Urho Mikkonen. ", end="Villahousut \n" )

# rivivaihto
teksti = "Tässä tekstissä on rivinvaihto. \n"
print(teksti)

# repr prints the text exactly how it was written in the code
raakateksti = repr(teksti)
print(raakateksti)

# round
luku1 = 3.5
luku2 = 4.123123
luku3 = 1234.1231513

luku1 = round(luku1)
luku2 = round(luku2,2)
luku3 = round(luku2,4)
print(luku1, luku2, luku3)

# if the string is too long it should be divided with \
print("Tämä lause on tarkoituksella kirjoitettu niin pitkäksi \
että teksti menee toiselle riville.")

print("Jokaiselle tulee joskus tunne että tarvitsisi sanoa \
      jotain mutta ei vain pysty valitsemaan mielenkiintoista \
      aihetta.")

teksti\
= "Jokaiselle tulee joskus tunne että tarvitsisi sanoa \
jotain mutta ei vain pysty valitsemaan mielenkiintoista \
aihetta."

print\
(teksti)

# """string in triple quotes"""" 
print("""Asunnonostajan tulee miettiä valmiiksi seuraavat asiat:
-talon hinta
-talon tyyppi
-sijainti
-remontit
-naapurusto
-koulut
-julkiset palvelut
-liikenneyhteydet""")

# \ \ formatting escape character
print("Muotoilumerkit sotkevat asioita: Pitäisikö tässä \ \
olla kaksi kenoviivaa, yksi kenoviiva ja virheilmoitus vai \ mitä?")

print("Hän sanoi \"Täällä tapahtuu muutoksia.\" ")
print('Mick O\'Malley')

# \n\n adds two lines beafore and after the string
print('\n\nRivinvaihtoja!\n\n')

# \t tabulaion in the text
print("Nimi:\tPekka Mikkonen")

# # input
# tallenne = input("Kuinka pitkä olet (cm):")
# print(tallenne)

# # program runs scripts one by one 
# nimi = input("Mikä on nimesi?: ")
# print("Hei",nimi+"!")

# for multiplying the number should be - int()
arvo = "313"
print(arvo * 2)
print(int(arvo) * 2)
print('Hepokatti' * 3)

# Luku on 3.14 tai 3.14159
pi = 3.141592635
print("Luku on {:2.2f} tai {:2.5f}".format(pi,pi))

# Sauli on 71 vuotta vanha
nimi = "Sauli"
ika = 71
print("{} on {} vuotta vanha".format(nimi, ika))

# Tehtävä 1
luku = 10
print('Kokonaislukumuunnos ei osaa pyöristää:', luku)
merkkijono = 'MerkkijonoMerkkijono'
print('Merkkijonon kertominen tuottaa toistoa:', merkkijono)

# Tehtävä 2
teksti = "Tämä on usean rivin tulostus:\n\
Teksti on jaettu usealle riville.\n\
Nimi:\tPetteri\n\
Ammatti:\tKartturi"
print(teksti)

# Tehtävä 3
print("Laskin")
luku1T = input("Anna ensimmäinen luku: ")
luku2T = input("Anna toinen luku: ")
tulosT = int(luku1T) + int(luku2T)
print("Tulos on:",tulosT) 