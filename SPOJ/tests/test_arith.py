from unittest import *

from SPOJ.arith import *


class TestArith(TestCase):
    def test_analyse_arith(self):
        input = "12345+67890"
        res = " 12345\n+67890\n------\n 80235"
        assert (analyse_arith(input) == res)

    def test_add_string_1(self):
        input1 = "125"
        input2 = "124"
        res = "249"
        assert (add_string(input1, input2) == res)

    def test_add_string_2(self):
        input1 = "125"
        input2 = "125"
        res = "250"
        assert (add_string(input1, input2) == res)

    def test_add_string_3(self):
        input1 = "2"
        input2 = "999"
        res = "1001"
        assert (add_string(input1, input2) == res)

    def test_add_string_4(self):
        input1 = "1"
        input2 = "999"
        res = "1000"
        assert (add_string(input1, input2) == res)

    def test_add_string_5(self):
        input1 = "16"
        input2 = "96"
        res = "112"
        assert (add_string(input1, input2) == res)
