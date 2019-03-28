def DATA_get(fichierName):
    if not(DATA_existe(fichierName)):
        DATA_set(fichierName,"")
    _tmp = open(fichierName,"r+")
    _contenu = _tmp.read()
    _tmp.close()
    return _contenu
def DATA_existe(fichierName):
    try:
        fichier = open(fichierName,"r")
        fichier.close()
        return True
    except:
        return False
def DATA_getLigne(fichierName,ligne):
    if not(DATA_existe(fichierName)):
        DATA_set(fichierName,"")
    _tmp = open(fichierName,"r+")
    for _i in range(ligne):
        _ligne=_tmp.readline()
    _tmp.close()
    try:
        return _ligne
    except:
        return ""
def DATA_set(fichierName,contenu):
    if DATA_existe(fichierName):
        _tmp = open(fichierName,"w+")
    else:
        _tmp = open(fichierName,"w")
    _tmp.write(str(contenu))
    _tmp.close()
    return
DATA_set("test.txt",1)
print(DATA_get("test.txt"))