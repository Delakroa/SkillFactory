import pytest
from Modul_19.Task_19_2_3.app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, x=6, y=3) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, x=10, y=5) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, x=3, y=3) == 6

