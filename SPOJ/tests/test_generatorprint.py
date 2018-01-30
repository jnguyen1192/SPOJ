from unittest import *

from SPOJ.generatorprint import *
import unittest


class TestPrint1(TestCase):
    @unittest.skip("")
    def test_primesRange_3_to_7(self):
        res = "3\n5\n7"

    def test_generator(self):
        generate()
        #assert (primesRange(2, 1000002, 1000000) == res)
