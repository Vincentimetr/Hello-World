import sqlite3 as lite

def SQL(query):
	print(len(query)*"_")
	print(query)
	print(len(query)*"-")
	BDD_name="BDD.db"
	con = lite.connect(BDD_name)
	con.row_factory = lite.Row
	cur = con.cursor()
	cur.execute(query)
	if (query[:6]=="SELECT"):
		_return = cur.fetchall()
		con.close()
		return _return
	elif (query[:6]=="UPDATE"):
		con.commit()
		con.close()
		return
	elif(query[:6]=="INSERT"):
		con.commit()
		con.close()
		return
	return
	
def affiche(SQL_return):
	MAXs=[]
	
	for i in range(len(SQL_return)):
		maxi=0
		for j in range(len(SQL_return[i])):
			maxi=max(maxi,len(str(SQL_return[i][j])))
		MAXs.append(maxi)
	string="|"
	for i in range(len(SQL_return)):
		for j in range(len(SQL_return[i])):
			data=str(SQL_return[i][j])
			string+=data+" "*(MAXs[i]-len(data))
			string+="|"
		string+="\n|"
	string+="\n"
	print(string[:-2])
	return

def Q(query):
	SQL_return=SQL(query)
	affiche(SQL_return)
	return SQL_return
	
Q1=Q("SELECT nom,secteur FROM Service")
Q2=Q("SELECT nom,secteur FROM Service ORDER BY nom ASC")
Q3=Q("SELECT tel FROM Client WHERE nom='{}'".format("Aupré"))
Q4=Q("SELECT AVG(salaire) FROM Employe AS salaire_moyen")
Q5=Q("SELECT qualite, AVG(salaire) FROM employe GROUP BY qualite")
Q6=Q("SELECT salaire FROM employe WHERE date_embauche>{}".format("2015-1-1"))