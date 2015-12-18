# -*- coding: utf-8 -*-


import os
import json
import unittest 

import utils

from agora_results.pipes.results import do_tallies

class results_tests(unittest.TestCase):
	
	def test_positive_check_config(self):
		config = utils.getConfigJson("res/config.json")
		self.assertTrue(do_tallies.check_config(config))

	def test_positive_execute(self):
		config = utils.getConfigJson("res/config.json")
		data = "574.tar.gz"

if __name__=='__main__':
   unittest.main()
