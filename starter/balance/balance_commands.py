"""Command package for balance operations"""

from transaction.transaction import Transaction

from abc import ABC, abstractmethod


class BalanceCommand(ABC):
    """Abstract class as base of command operations"""

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class AddIncome(BalanceCommand):
    def __init__(self, balance):
        super().__init__()
        self._balance = balance
        self._previous_amount = [0]

    def execute(self, amount):
        self._previous_amount.append(amount)
        self._balance.add_income(amount)

    def undo(self):
        self._balance.add_expense(self._previous_amount.pop())


class AddExpense(BalanceCommand):
    def __init__(self, balance):
        super().__init__()
        self._balance = balance
        self._previous_amount = []

    def execute(self, amount):
        self._previous_amount.append(amount)
        self._balance.add_expense(amount)

    def undo(self):
        self._balance.add_income(self._previous_amount.pop())


class ApplyTransaction(BalanceCommand):
    def __init__(self, balance):
        super().__init__()
        self._balance = balance

    def execute(self, transaction: Transaction):
        self._balance.apply_transaction(transaction)

    def undo(self):
        self._balance._balance = 0
