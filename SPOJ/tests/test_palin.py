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
        res = "313\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_8(self):
        input = "199\n"
        res = "212\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_9(self):
        input = "952\n"
        res = "959\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_10(self):
        input = "95152\n"
        res = "95159\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_11(self):
        input = "11111111111111111111211111111111111111111\n"
        res =   "11111111111111111111311111111111111111111\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_12(self):
        input = "123456789123456789123456789\n"
        res =   "123456789123464321987654321\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_13(self):
        input = "123456789123454789123456789\n"
        res =   "123456789123464321987654321\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_14(self):
        input = "999\n"
        res =   "1111\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_15(self):
        input = "123456789\n"
        res = "123464321\n"
        assert (analyse_palin(input) == res)

    def test_analyse_palin_16(self):
        input = "1112112\n"
        res = "1113111\n"
        assert (analyse_palin(input) == res)

    def test_add1tostring_1(self):
        input = "19"
        res = "20"
        assert (add1tostring(input) == res)

    def test_add1tostring_2(self):
        input = "129"
        res = "130"
        assert (add1tostring(input) == res)

    def test_add1tostring_3(self):
        input = "999"
        res = "1000"
        assert (add1tostring(input) == res)

    def test_add1tostring_4(self):
        input = "199999"
        res =   "200000"
        assert (add1tostring(input) == res)

    def test_add1tostring_5(self):
        input = "91119"
        res =   "91120"
        assert (add1tostring(input) == res)

    def test_is_palin_1(self):
        input = "91119"
        assert (is_palin(input))

    def test_is_palin_2(self):
        input = "91120"
        assert (not is_palin(input))

    def test_is_palin_3(self):
        input = "9119"
        assert (is_palin(input))

    def test_is_palin_4(self):
        input = "9120"
        assert (not is_palin(input))

    def test_is_palin_5(self):
        input = "818"
        assert (is_palin(input))
