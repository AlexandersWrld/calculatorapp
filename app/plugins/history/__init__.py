from app.commands import Command
import sys
sys.path.append('../../IS218_HW3_revised')
from decimal import Decimal, InvalidOperation
from calculator import Calculator
from calculator.calculation import Calculation
from calculator.calchistory import CalculationHistory
from calculator.arithmetic import add, subtract, multiply, divide

class HistoryCommand(Command):
    
    def execute(self):
        appHistory = Calculator.getHistory()
        print(appHistory)