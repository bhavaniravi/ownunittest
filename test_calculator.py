from ownunittest import TestCase
from ownunittest import main

# from unittest import TestCase

from calculator import Calculator
import logging
import pytest


class TestCalculator(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_zero(self):
        with self.assertRaises(TypeError):
            self.calc.divide(6, 0)

    def test_add_strings(self):
        for item in [
            {"input": ("1", "2"), "output": "12"},
            {"input": ([], [1, 2]), "output": [1, 2]},
            {"input": (1, 1), "output": 2},
        ]:
            ip, output = item["input"], item["output"]
            print(f"ip: {ip}, output: {output}")
            with self.subTest(ip=ip, output=output):
                self.assertEqual(self.calc.add(*ip), output)


if __name__ == "__main__":
    main()
