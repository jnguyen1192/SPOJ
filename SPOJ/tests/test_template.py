from unittest import *

from SPOJ.template import *


class TestTemplate(TestCase):
    def test_analyse_template(self):
        input = "template\n"
        res = "template\n"
        assert (analyse_template(input) == res)
