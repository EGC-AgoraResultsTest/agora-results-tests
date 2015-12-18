import os
import json

def executeAgoraResults(tally):
	# Ejecutamos Agora-Results con el caso a prueba a probar.
  	# El resultado lo guardamos en un archivo, en formato Json
	os.system('agora-results -t res/'+tally+'.tar.gz -c res/config.json -s > results')		

def getJsonObjectFromResults():

	# Abrimos el archivo previamente guardado con el resultado de la prueba
	f = open("results", "r")
	# Leemos el archivo
	data = f.read()
	# Cerramos el archivo
	f.close()	

	# Devolvemos como objeto Json los datos del archivo
	return json.loads(data)

def getConfigJson(path):
	f = open(path, "r")
	data = f.read()
	f.close()
	return json.loads(data)
