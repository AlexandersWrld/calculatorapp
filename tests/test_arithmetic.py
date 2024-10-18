from calculator.calculation import Calculation
from calculator import add, subtract, divide, multiply

def test_addition():  
    calculation = Calculation(2, 2, add)  
    assert calculation.docalculation() == 4

def test_subtraction():
    calculation = Calculation(7, 2, subtract)  
    assert calculation.docalculation() == 5
    
def test_multiplication():
    calculation = Calculation(7, 3, multiply)  
    assert calculation.docalculation() == 21

def test_division():
    calculation = Calculation(27, 3, divide)
    assert calculation.docalculation() == 9