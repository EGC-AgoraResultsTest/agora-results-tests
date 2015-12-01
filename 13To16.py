# -*- coding: utf-8 -*-

import os
import json
import unittest 


class Test13To16(unittest.TestCase):

	# Prueba de votos válidos en una situación en la que min=2 y max=4
	# Asignado a: test-valid_votes_with_min2max4.tar.gz
	def test_valid_votes_in_min2max4_situation(self):
		os.system('agora-results -t testCases/test-valid_votes_with_min2max4.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		jsonObjectAnswers = jsonObject["questions"][0]["answers"]

		self.assertEqual(jsonObjectAnswers[0]["winner_position"], 0)
		self.assertEqual(jsonObjectAnswers[1]["winner_position"], None)

		self.assertEqual(jsonObjectAnswers[0]["text"], "Opcion 2")

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 4)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)

	# Prueba de votos inválidos saliendo del rango en una situación en la que min=2 y max=4
	# Asignado a: test-invalid_votes_with_min2max4.tar.gz
	def test_invnalid_votes_in_min2max4_situation(self):
		os.system('agora-results -t testCases/test-invalid_votes_with_min2max4.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		jsonObjectAnswers = jsonObject["questions"][0]["answers"]

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 3)

	
if __name__=='__main__':
   unittest.main()
