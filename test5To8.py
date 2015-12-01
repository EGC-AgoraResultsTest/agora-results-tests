# -*- coding: utf-8 -*-

import os
import json
import unittest 


class Test5To8(unittest.TestCase):

	# Prueba en la que no haya votos
	# Asignado a: test-empty_votes.tar.gz
	def test_05(self):
		os.system('agora-results -t testCases/test-empty_votes.tar.gz -s > results') 

		f = open("results", "r")
		data = f.read()
		f.close() 

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)

	# Prueba en la que no haya ganador si no hay votos
	# Asignado a: test-no_winner_with_no_votes.tar.gz
	def test_no_winner_with_no_votes(self):
		os.system('agora-results -t testCases/test-no_winner_with_no_votes.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		jsonObjectAnswers = jsonObject["questions"][0]["answers"]

		self.assertEqual(jsonObjectAnswers[0]["winner_position"], None)
		self.assertEqual(jsonObjectAnswers[1]["winner_position"], None)
		self.assertEqual(jsonObjectAnswers[2]["winner_position"], None)

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)
		
if __name__=='__main__':
   unittest.main()
