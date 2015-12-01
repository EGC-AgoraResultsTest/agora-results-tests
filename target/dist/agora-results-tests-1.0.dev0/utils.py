import os
import json

def executeAgoraResults(tally):

	os.system('agora-results -t res/'+tally+'.tar.gz -s > results')		

def getJsonObjectFromResults():

	# Abrimos el archivo previamente guardado con el resultado de la prueba
	f = open("results", "r")
	# Leemos el archivo
	data = f.read()
	# Cerramos el archivo
	f.close()	

	# Devolvemos como objeto Json los datos del archivo
	return json.loads(data)
