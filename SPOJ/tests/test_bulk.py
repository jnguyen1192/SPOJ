from unittest import *

from SPOJ.bulk import *


class TestBulk(TestCase):
    def test_analyse_poly(self):
        input = "4  0 0 200  10 0 200  10 10 200  0 10 200"
        res = "['4', '0 0 200', '10 0 200', '10 10 200', '0 10 200']"
        assert (analyse_poly(input) == res)
