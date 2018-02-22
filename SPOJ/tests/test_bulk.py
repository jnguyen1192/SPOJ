from unittest import *

from SPOJ.bulk import *


class TestBulk(TestCase):
    def test_analyse_bulk(self):
        input = "bulk\n"
        res = "bulk\n"
        assert (analyse_bulk(input) == res)
