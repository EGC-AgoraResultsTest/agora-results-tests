import os
import json
import unittest 


class TestStringMethods(unittest.TestCase):

	def test_empty_votes(self):
		os.system('agora-results -t testCases/test-empty_votes.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)

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

	def test_no_winner_with_blank_votes(self):
		os.system('agora-results -t testCases/test-no_winner_with_blank_votes.tar.gz -s > results')		

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
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 7)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)
	
	def test_no_winner_with_null_votes(self):
		os.system('agora-results -t testCases/test-no_winner_with_null_votes.tar.gz -s > results')		

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
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 5)

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

	def test_winner_in_ordinary_situation_with2maxwinners(self):
		os.system('agora-results -t testCases/test-winner_in_ordinary_situation_with2maxwinners.tar.gz -s > results')		

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

	def test_tie_in_ordinary_situation_with2maxwinners(self):
		os.system('agora-results -t testCases/test-tie_in_ordinary_situation_with2maxwinners.tar.gz -s > results')		

		f = open("results", "r")
		data = f.read()
		f.close()	

		jsonObject = json.loads(data)

		jsonObjectTotalVotes = jsonObject["questions"][0]["totals"]

		jsonObjectAnswers = jsonObject["questions"][0]["answers"]

		self.assertEqual(jsonObjectAnswers[0]["winner_position"], 0)
		self.assertEqual(jsonObjectAnswers[1]["winner_position"], 1)
		self.assertEqual(jsonObjectAnswers[2]["winner_position"], None)

		self.assertEqual(jsonObjectAnswers[0]["text"], "Opcion 1")
		self.assertEqual(jsonObjectAnswers[1]["text"], "Opcion 2")

		self.assertEqual(jsonObjectTotalVotes["valid_votes"], 4)
		self.assertEqual(jsonObjectTotalVotes["blank_votes"], 0)
		self.assertEqual(jsonObjectTotalVotes["null_votes"], 0)

		
if __name__=='__main__':
   unittest.main()

