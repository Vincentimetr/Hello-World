def affichage_heure ():
    import time
    a="Depuis 1970 le premier janvier il s'est ecoule: "
    b=str(time.time())
    c=" secondes"
    print (a+b+c)
    return

def exercice1 ():
    print("Hello World")
    return

def exercice2 ():
    print("Hello",end=" ")
    print("World")
    return

def exercice3 ():
    a="Hello "
    b="World"
    print(a+b)
    return

def exercice4 ():
    a=""
    a+=chr(72)
    a+=chr(101)
    a+=chr(108)
    a+=chr(108)
    a+=chr(111)
    a+=chr(32)
    a+=chr(87)
    a+=chr(111)
    a+=chr(114)
    a+=chr(108)
    a+=chr(100)
    print(a)
    return

