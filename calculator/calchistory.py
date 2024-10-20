from calculator.calculation import Calculation
from typing import List

class CalculationHistory:
    history: List[Calculation] = []

    @classmethod
    def addToHistory(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def retrieveHistory(cls) -> List[Calculation]:
        return cls.history
    
    @classmethod
    def lastCalculation(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def clearHistory(cls):
        cls.history.clear()

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]