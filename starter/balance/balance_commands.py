"""Command package for balance operations"""


from abc import ABC, abstractmethod


class BalanceCommand(ABC):
    """Abstract class as base of command operations"""

    def __init__(self, balance):
        self._balance = balance
        self._previous_balance = 0

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class ResetBalance(BalanceCommand):
    def __init__(self, balance):
        super().__init__(balance)

    def execute(self):
        self._previous_balance = self._balance._balance
        self._balance.reset()

    def undo(self):
        self._balance.add_income(self._previous_balance)
