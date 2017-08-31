from one_line_calculator.calculator import *

class TestClass(object):
    def test_one(self):
        a = 1
        b = 2
        c = 3
        assert addition(a, b) == c
