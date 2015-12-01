# -*- coding: utf-8 -*-

import os
import json
import unittest 


class Test1To4(unittest.TestCase):

	# Prueba de un caso en el que todos los votos sean válidos
	# Asociado a: test-valid_votes.tar.gz
	def test_01(self):
		# Ejecutamos Agora-Results con el caso a prueba a probar.
  		# El resultado lo guardamos en un archivo, en formato Json
		os.system('agora-results -t testCases/test-valid_votes.tar.gz -s > results')		

		# Abrimos el archivo previamente guardado con el resultado de la prueba
		f = open("results", "r")
		# Leemos el archivo
		data = f.read()
		# Cerramos el archivo
		f.close()	

		# Cargamos como objeto Json los datos del archivo
		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 4)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)

		
if __name__=='__main__':
   unittest.main()

