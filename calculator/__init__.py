from calculator.arithmetic import add, subtract, multiply, divide
from calculator.calchistory import CalculationHistory
from calculator.calculation import Calculation

class Calculator:
    @staticmethod
    def _perform_operation(a, b, operation):
        calculation = Calculation.newcalculation(a, b, operation)
        CalculationHistory.addToHistory(calculation)
        return calculation.docalculation()
    
    @staticmethod
    def getHistory(): 
        return CalculationHistory.retrieveHistory() 

    @staticmethod    
    def add(a,b):
        calculation = Calculation(a, b, add)
        return calculation.docalculation()
    
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)
        return calculation.docalculation()
    
    @staticmethod
    def multiply(a,b):
        calculation = Calculation(a, b, multiply)
        return calculation.docalculation()
    
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)
        return calculation.docalculation()