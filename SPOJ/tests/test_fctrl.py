from unittest import *

from SPOJ.fctrl import *


class TestFctrl(TestCase):
    def test_analyse_fctrl_1(self):
        input = 3
        res = "0"
        assert (analyse_fctrl(input) == res)

    def test_analyse_fctrl_2(self):
        input = 60
        res = "14"
        assert (analyse_fctrl(input) == res)

    def test_analyse_fctrl_3(self):
        input = 100
        res = "24"
        assert (analyse_fctrl(input) == res)

    def test_analyse_fctrl_4(self):
        input = 1024
        res = "253"
        assert (analyse_fctrl(input) == res)

    def test_analyse_fctrl_5(self):
        input = 23456
        res = "5861"
        assert (analyse_fctrl(input) == res)

    def test_analyse_fctrl_6(self):
        input = 8735373
        res = "2183837"
        assert (analyse_fctrl(input) == res)
