from calculator import Calculator
import pytest

def test_add():
    assert Calculator.add(2,3) == 5

def test_subtraction():
    assert Calculator.subtract(8,2) == 6

def test_multiplication():
    assert Calculator.multiply(7,3) == 21

def test_division():
    assert Calculator.divide(27,3) == 9