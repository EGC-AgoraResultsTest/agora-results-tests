# -*- coding: utf-8 -*-

import os
import json
import unittest 

import utils


class OneToFour_Tests(unittest.TestCase):

	# Prueba de un caso en el que todos los votos sean válidos
	# Asociado a: test_01.tar.gz
	def test_01(self):
		# Ejecutamos Agora-Results con el caso a prueba a probar.
  		# El resultado lo guardamos en un archivo, en formato Json
		os.system('agora-results -t res/test_01.tar.gz -s > results')		

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

	# Prueba en el que todos los vatos sean en blanco
	# Asociado a: test_02.tar.gz
	def test_02(self):
		os.system('agora-results -t res/test_02.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 4)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)
	
	# Prueba en el que todos los votos son en nulo
	# Asociado a: test_03.tar.gz
	def test_03(self):
		os.system('agora-results -t res/test_03.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 4)

	# Prueba en el que haya una variedad de votos (nulos, blancos y válidos)
	# Asociado a: test_04.tar.gz
	def test_04(self):
		os.system('agora-results -t res/test_04.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 2)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 2)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 2)
		
if __name__=='__main__':
   unittest.main()

