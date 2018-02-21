from unittest import *

from SPOJ.arith import *


class TestArith(TestCase):
    def test_analyse_arith_add(self):
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

    def test_add_string_print_case_str2_longest(self):
        input1 = "12345"
        input2 = "67890"
        res = " 12345\n+67890\n------\n 80235"
        print add_string_print(input1, input2)
        assert (add_string_print(input1, input2) == res)

    def test_add_string_print_case_str1_longest(self):
        input1 = "1234"
        input2 = "4"
        res = "1234\n  +4\n----\n1238"
        print add_string_print(input1, input2)
        assert (add_string_print(input1, input2) == res)

    def test_add_string_print_case_res_longest(self):
        input1 = "9999"
        input2 = "15"
        res = " 9999\n  +15\n-----\n10014"
        print add_string_print(input1, input2)
        assert (add_string_print(input1, input2) == res)

    def test_sub_string_1(self):
        input1 = "125"
        input2 = "124"
        res = "1"
        assert (sub_string(input1, input2) == res)

    def test_sub_string_2(self):
        input1 = "125"
        input2 = "125"
        res = "0"
        assert (sub_string(input1, input2) == res)

    def test_sub_string_3(self):
        input1 = "1001"
        input2 = "2"
        res = "999"
        assert (sub_string(input1, input2) == res)

    def test_sub_string_4(self):
        input1 = "999"
        input2 = "1"
        res = "998"
        assert (sub_string(input1, input2) == res)

    def test_sub_string_5(self):
        input1 = "95"
        input2 = "16"
        res = "79"
        assert (sub_string(input1, input2) == res)

    def test_mul_string_1(self):
        input1 = "325"
        input2 = "0"
        res = "0"
        assert (mul_string(input1, input2) == res)

    def test_mul_string_2(self):
        input1 = "325"
        input2 = "4"
        res = "1300"
        assert (mul_string(input1, input2) == res)

    def test_mul_string_3(self):
        input1 = "1234"
        input2 = "4"
        res = "4936"
        assert (mul_string(input1, input2) == res)

    def test_mul_string_4(self):
        input1 = "999"
        input2 = "1"
        res = "999"
        assert (mul_string(input1, input2) == res)

    def test_mul_string_5(self):
        input1 = "95"
        input2 = "6"
        res = "570"
        assert (mul_string(input1, input2) == res)

    def test_mul_string_6(self):
        input1 = "1000"
        input2 = "6"
        res = "6000"
        assert (mul_string(input1, input2) == res)

    def test_mul_string_7(self):
        input1 = "9502000202151515150505151515106061615150505151451505020515154544151358768453123203156165165135131515103220321351561612032035453153213213"
        input2 = "0"
        res = "0"
        assert (mul_string(input1, input2) == res)

    def test_mul_string_8(self):
        input1 = "9502000202151515150505151515106061615150505151451505020515154544151358768453123203156165165135131515103220321351561612032035453153213213"
        input2 = "1"
        res = "9502000202151515150505151515106061615150505151451505020515154544151358768453123203156165165135131515103220321351561612032035453153213213"
        assert (mul_string(input1, input2) == res)