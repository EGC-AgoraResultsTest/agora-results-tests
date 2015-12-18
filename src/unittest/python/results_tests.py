# -*- coding: utf-8 -*-


import os
import json
import unittest 

import utils

import agora_results.pipes.results

class results_tests(unittest.TestCase):
	
	def test_positive_check_config(self):
		config = utils.getConfigJson("res/config.json")
		self.assertTrue(config)

if __name__=='__main__':
   unittest.main()
