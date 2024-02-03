# len
merkkijono = "Lentoturbiinihuoltotoimintotukihenkilö"
print(len(merkkijono))
print(merkkijono[0])
print(merkkijono[-1])
print(merkkijono[-0])
print(merkkijono[0:10])
print(merkkijono[0:33:2])
print(merkkijono[34:0:-1])
print(merkkijono[7:len(merkkijono)])
print(merkkijono[5:])
print(merkkijono[:15])
print(merkkijono[25::2])
print(merkkijono[::-1])

# STRING METHODS
merkkijono2 = 'Sininen'

# upper()
merkkijono2_isolla = merkkijono2.upper()
# lower()
merkkijono2_pienella = merkkijono2.lower()

# find('')
sijainti = merkkijono2.find('nin')
# replace('', '')
muutettu = merkkijono2.replace('i', 'o')
# isalpha()
testi_1 = merkkijono2.isalpha()
# isdigit()
testi_2 = merkkijono2.isdigit()
# endswith('')
testi_3 = merkkijono2.endswith('nen')

print(merkkijono2_isolla, merkkijono2_pienella, muutettu)
print("Merkkijono 'nin' on paikasta",sijainti,"eteenpäin.")
print(testi_1,": merkkijono sisältää pelkästään kirjaimia.")
print(testi_2,": jono ei ole numeroarvo.")
print(testi_3,": merkkijono loppuu merkkeihin 'nen'")

# variables adding
mjono1 = 'Hello '
mjono2 = 'world'
print(mjono1+mjono2) 

# variable repeating
print(mjono1*4) 

# variable comparing
print(mjono1 == mjono2)
print(mjono1 != mjono2)

# Tehtävä
merkkijonoT = 'Hattukauppias'
print("Muuttujan 4 ensimmäistä kirjainta ovat",merkkijonoT[:4])
print("Muuttujan 4 viimeistä kirjainta ovat",merkkijonoT[-4:])
print("Muuttujan teksti on väärinpäin",merkkijonoT[::-1])
