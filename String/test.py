def affiche1(data):
	return print(str(data))

def affiche2(data):
	return print(len(str(data))*"-"+"\n"+str(data)+"\n"+len(str(data))*"-")

def affiche3(data,max):
	return print(max*"-"+"\n"+data[:max]+"\n"+max*"-")