"""Command package for balance operations"""

from transaction.transaction import Transaction, TransactionCategory

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
    def __init__(self, balance, amount):
        super().__init__()
        self._balance = balance
        self._amount = amount

    def execute(self):
        self._balance.add_income(self._amount)

    def undo(self):
        self._balance.add_expense(self._amount)

    def describe_last_transaction(self):
        return f"Add income: ${self._amount}."


class AddExpense(BalanceCommand):
    def __init__(self, balance, amount):
        super().__init__()
        self._balance = balance
        self._amount = amount

    def execute(self):
        self._balance.add_expense(self._amount)

    def undo(self):
        self._balance.add_income(self._amount)

    def describe_last_transaction(self):
        return f"Add expense: ${self._amount}."


class ApplyTransaction(BalanceCommand):
    def __init__(self, balance):
        super().__init__()
        self._balance = balance
        self._previous_transactions = []

    def execute(self, transaction: Transaction):
        self._previous_transactions.append(transaction)
        self._balance.apply_transaction(transaction)

    def undo(self):
        previous = self._previous_transactions.pop()
        if previous.category == TransactionCategory.INCOME:
            previous.category = TransactionCategory.EXPENSE
        else:
            previous.category = TransactionCategory.INCOME
        self._balance.apply_transaction(previous)
        
    def describe(self):
        previous = self._previous_transactions[-1]
        return f"Apply transaction: ${previous.amount} {previous.category.value.upper()}."


class GetBalance(BalanceCommand):
    def __init__(self, balance):
        super().__init__()
        self._balance = balance

    def execute(self):
        return self._balance.get_balance()

    def undo(self):
        pass


class GetSummary(BalanceCommand):
    def __init__(self, balance):
        super().__init__()
        self._balance = balance

    def execute(self):
        return self._balance.summary()

    def undo(self):
        pass
