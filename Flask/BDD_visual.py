import sys
sys.path.insert(0,"C:\Drive\Python\BDD")
from BDD import *

from flask import Flask
from flask import render_template
from flask import request

#Initialisations
app = Flask(__name__)
# @app.route('/')

tablesList=SQL_getTables()
for i in range(len(tablesList)):
    table=tablesList[i]
    print(table)
    fun=\
'''
@app.route('/'+table)
def {}():\n
    nom=tablesList[i]
    colonnes=SQL_getColonnes(nom)
    data=SQL_getTable(nom)
    lignes=len(data)
    return render_template('table.html',colonnes=colonnes,data=data,table=nom,lignes=lignes)
'''.format(table)
exec(fun)
@app.route('/all')
def all():
    tables=[]
    tablesList=SQL_getTables()
    for i in tablesList:
        table={}
        tableValues=SQL_getTable(i)
        colonnes=SQL_getColonnes(i)
        nomColonnes=[]
        for j in colonnes:
            nomColonnes.append(i+"."+j)
        table['colonnes']=nomColonnes
        table['values']=[]
        for j in tableValues:
            ligne=[]
            for k in j:
                ligne.append(k)
            table['values'].append(ligne)
        tables.append(table)
    return render_template('all.html',tables=tables)

@app.route('/relationnel')
def relationnel():
    tables=[]
    tablesList=SQL_getTables()
    for i in tablesList:
        table={}
        table['nom']=i
        table['colonnes']=SQL_getColonnes(i)
        tables.append(table)
    return render_template('relationnel.html',tables=tables)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5571)

