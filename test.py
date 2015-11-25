import os
import json
import unittest 


class TestStringMethods(unittest.TestCase):

	def test_example(self):
		# Ejecutamos Agora-Results con el caso a prueba a probar.
  		# El resultado lo guardamos en un archivo, en formato Json
		os.system('agora-results -t testCases/test.tar.gz -s > results')		

		# Abrimos el archivo previamente guardado con el resultado de la prueba
		f = open("results", "r")
		# Leemos el archivo
		data = f.read()
		# Cerramos el archivo
		f.close()	

		# Cargamos como objeto Json los datos del archivo
		jsonObject = json.loads(data)

		print("Votos totales: "+str(jsonObject["total_votes"]))
		self.assertEqual(jsonObject["total_votes"], 4)

if __name__=='__main__':
   unittest.main()

