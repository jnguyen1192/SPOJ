from unittest import *

from SPOJ.palin import *


class TestPalin(TestCase):
    def test_analyse_palin_1(self):
        input = "808\n"
        res = "818\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_2(self):
        input = "2133\n"
        res = "2222\n"
        print analyse_palin(input)
        assert (analyse_palin(input) == res)
