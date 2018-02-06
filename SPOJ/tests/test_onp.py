from unittest import *

from SPOJ.onp import *


class TestOnp(TestCase):
    def test_analyse_onp_1(self):
        input = "(a+(b*c))\n"
        res = "abc*+\n"
        assert (analyse_onp(input) == res)

    def test_analyse_onp_2(self):
        input = "((a+b)*(z+x))\n"
        res = "ab+zx+*\n"
        assert (analyse_onp(input) == res)

    def test_analyse_onp_3(self):
        input = "((a+t)*((b+(a+c))^(c+d)))\n"
        res = "at+bac++cd+^*\n"
        assert (analyse_onp(input) == res)
