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
        assert (analyse_palin(input) == res)

    def test_analyse_palin_3(self):
        input = "2933\n"
        res = "2992\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_4(self):
        input = "2792\n"
        res = "2882\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_5(self):
        input = "2092\n"
        res = "2112\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_6(self):
        input = "202\n"
        res = "212\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_7(self):
        input = "292\n"
        res = "303\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_8(self):
        input = "199\n"
        res = "202\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_9(self):
        input = "952\n"
        res = "959\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_10(self):
        input = "95152\n"
        res = "95159\n"
        assert (analyse_palin(input) == res)

    def test_add1tostring_1(self):
        input = "19"
        res = "20"
        assert (add1tostring(input) == res)

    def test_add1tostring_2(self):
        input = "129"
        res = "130"
        assert (add1tostring(input) == res)
