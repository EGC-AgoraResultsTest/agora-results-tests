# -*- coding: utf-8 -*-

import os
import json
import unittest 


class Test5To8(unittest.TestCase):

	# Prueba en la que existe un ganador bajo una situación normal
	# Asignado a: test-winner_in_ordinary_situation.tar.gz
	def test_winner_in_ordinary_situation(self):
		os.system('agora-results -t testCases/test-winner_in_ordinary_situation.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		jsonObjectAnswers = jsonObject["questions"][0]["answers"]

		self.assertEqual(jsonObjectAnswers[0]["winner_position"], 0)
		self.assertEqual(jsonObjectAnswers[1]["winner_position"], None)
		self.assertEqual(jsonObjectAnswers[2]["winner_position"], None)

		self.assertEqual(jsonObjectAnswers[0]["text"], "Opcion 2")

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 8)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 1)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 1)
	
	# Prueba en la que existe un empate bajo una situación normal
	# Asignado a: test-tie_in_ordinary_situation.tar.gz
	def test_tie_in_ordinary_situation(self):
		os.system('agora-results -t testCases/test-tie_in_ordinary_situation.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		jsonObjectAnswers = jsonObject["questions"][0]["answers"]

		self.assertEqual(jsonObjectAnswers[0]["winner_position"], None)
		self.assertEqual(jsonObjectAnswers[1]["winner_position"], None)
		self.assertEqual(jsonObjectAnswers[2]["winner_position"], None)

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 4)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)

if __name__=='__main__':
   unittest.main()
