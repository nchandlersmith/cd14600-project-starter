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
    def __init__(self, balance, transaction):
        super().__init__()
        self._balance = balance
        self._transaction = transaction

    def execute(self):
        self._balance.apply_transaction(self._transaction)

    def undo(self):
        undo_transaction = None
        if self._transaction.category == TransactionCategory.INCOME:
            undo_transaction = Transaction(self._transaction.amount, TransactionCategory.EXPENSE)
        else:
            undo_transaction = Transaction(self._transaction.amount, TransactionCategory.INCOME)
        self._balance.apply_transaction(undo_transaction)
        
    def describe(self):
        return f"Apply transaction: ${self._transaction.amount} {self._transaction.category.value.upper()}."


class GetBalance(BalanceCommand):
    def __init__(self, balance):
        super().__init__()
        self._balance = balance

    def execute(self):
        return self._balance.get_balance()

    def undo(self):
        raise NotImplementedError("Get balance cannot be undone.")


class GetSummary(BalanceCommand):
    def __init__(self, balance):
        super().__init__()
        self._balance = balance

    def execute(self):
        return self._balance.summary()

    def undo(self):
        raise NotImplementedError("Get summary cannot be undone.")
