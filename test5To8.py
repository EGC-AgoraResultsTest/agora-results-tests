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
		
if __name__=='__main__':
   unittest.main()
