# Tehtävä 1

def main():
    print('''Supermarket
===========
''', end='')
    hinnat = [10,14,22,33,44,13,22,55,66,77]
    yhteensa = 0
    vaihto = 12
    
    while True:
        valinta = int(input('Valitse tuote (1-10) 0 lopetus: '))
        
        if (valinta > 0 and valinta <= 10):
            print('Tuote:  ',valinta,'Hinta:  ',hinnat[valinta - 1])
            yhteensa += hinnat[valinta - 1]
            maksu = yhteensa + vaihto
            
        elif(valinta == 0):
            print('Yhteensä:  ',yhteensa)
            print('Maksu: ',maksu)
            print('vaihto:  ',vaihto)
            break

if __name__ == '__main__':
    main()