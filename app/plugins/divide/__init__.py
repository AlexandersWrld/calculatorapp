from app.commands import Command
import sys
sys.path.append('../../IS218_HW3_revised')
from decimal import Decimal, InvalidOperation
from calculator import Calculator
from calculator.calculation import Calculation
from calculator.calchistory import CalculationHistory
from calculator.arithmetic import add, subtract, multiply, divide
from data import appData

class DivideCommand(Command):

    def execute(self):
        try:    
            number_1 = int(input('Enter the number you wish to divide: '))
            number_2 = int(input('Enter the number you want to divide it by: '))
            number_3 = Calculator._perform_operation(number_1, number_2, divide)
            appData.add_record("divide", number_1, number_2, number_3)
            print(number_3)
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")




            
        