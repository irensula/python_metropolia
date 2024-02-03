# moduuli tehtävälle 10/3

def testaa(salasana):
    if(len(salasana) > 5):
        luku = False
        kirjain = False
    
        for char in salasana:
            if char.isalpha():
                kirjain = True
            if char.isdigit():
                luku = True
            
        return luku and kirjain
    else:
        return False
print(testaa('52k')) 