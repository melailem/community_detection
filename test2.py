#!/usr/bin/env python3

import math
import unittest
from pylouvain import PyLouvain

class PylouvainTest(unittest.TestCase):
	def test_arxiv(self):
        	pyl = PyLouvain.from_file("data/arxiv.txt")
        	partition, q = pyl.apply_method()
		print q



if __name__ == '__main__':
	unittest.main()
