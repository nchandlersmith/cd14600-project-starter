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

    @abstractmethod
    def description(self):
        pass


class ResetBalance(BalanceCommand):
    def __init__(self, balance):
        super().__init__(balance)

    def execute(self):
        self._balance.reset()
    
    def undo(self):
        return super().undo()