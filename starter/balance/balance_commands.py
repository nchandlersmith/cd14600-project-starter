"""Command package for balance operations"""


from abc import ABC, abstractmethod


class BalanceCommand(ABC):
    """Abstract class as base of command operations"""

    def __init__(self, balance):
        self._balance = balance

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
        
        
class AddIncome(BalanceCommand):
    def __init__(self, balance):
        super().__init__(balance)
        self._previous_amount = [0]
        
    def execute(self, amount):
        self._previous_amount.append(amount)
        self._balance.add_income(amount)
    
    def undo(self):
        self._balance.add_expense(self._previous_amount.pop())
