import math
from unittest import TestCase

import hackone


class TestHackOne(TestCase):
    def test_one_is_two(self):
        assert 1 == 2

    def test_one_plus_one_is_four(self):
        assert 1 + 1 == 4

    def test_two_raised_to_the_one(self):
        assert 2 ** 1 == 4

    def test_two_minus_one(self):
        assert 2 - 1 == 0

    def test_log_one(self):
        assert math.exp(math.log(1)) == 2.0
