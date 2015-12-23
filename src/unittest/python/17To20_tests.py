# -*- coding: utf-8 -*-

import os
import json
import unittest 

import utils

class Test17To20(unittest.TestCase):

	# Prueba que el máximo de ganadores no puede ser 0
	# Asignado a: test_17.tar.gz
	def test_max_winners_cant_be_0(self):
		utils.executeAgoraResults('test_17')
		self.assertRaises(ValueError, utils.getJsonObjectFromResults)	

	# Prueba que el máximo de ganadores no puede ser mayor que el número de propuestas
	# Asignado a: test_18.tar.gz
	def test_max_winners_cant_be_greater_than_number_of_options(self):
		utils.executeAgoraResults('test_18')
		jsonData = utils.getJsonObjectFromResults()

		max_winners = jsonData["questions"][0]["num_winners"]
		number_options = len(jsonData["questions"][0]["answers"])

		self.assertRaises(AssertionError, self.assertTrue, number_options > max_winners)	

	# Prueba que el mínimo de opciones a seleccionar no sea menor que el mínimo
	# Asignado a: test_19.tar.gz
	def test_min_cant_be_greater_than_max(self):
		utils.executeAgoraResults('test_19')
		self.assertRaises(ValueError, utils.getJsonObjectFromResults)	

	# Prueba que el máximo y el mínimo de opciones a seleccionar no sean cero
	# Asignado a: test_20.tar.gz
	def test_max_and_min_cant_be_0(self):
		utils.executeAgoraResults('test_20')
		self.assertRaises(ValueError, utils.getJsonObjectFromResults)	

	
if __name__=='__main__':
   unittest.main()
