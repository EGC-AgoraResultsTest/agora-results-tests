# -*- coding: utf-8 -*-

import os
import json
import unittest 

import utils

class Test17To20(unittest.TestCase):

	# Prueba que el máximo de ganadores no puede ser 0
	# Asignado a: test_17.tar.gz
	def test_max_winners_cant_be_0(self):
		self.assertRaises(ValueError, utils.executeAgoraResults, 'test_17')	

	# Prueba que el máximo de ganadores no puede ser mayor que el número de propuestas
	# Asignado a: test_18.tar.gz
	def test_max_winners_cant_be_greater_than_number_of_options(self):
		self.assertRaises(ValueError, utils.executeAgoraResults, 'test_18')	

	# Prueba que el máximo de opciones a seleccionar no sea mayor a mínimo
	# Asignado a: test_19.tar.gz
	def test_max_options_cant_be_greater_than_min(self):
		self.assertRaises(ValueError, utils.executeAgoraResults, 'test_19')	

	# Prueba que el máximo y el mínimo de opciones a seleccionar no sean cero
	# Asignado a: test_20.tar.gz
	def test_max_and_min_cant_be_0(self):
		self.assertRaises(ValueError, utils.executeAgoraResults, 'test_20')	

	
if __name__=='__main__':
   unittest.main()
