# balance.py

from transaction.transaction_category import TransactionCategory
from balance.balance_observer import IBalanceObserver


class Balance:
    """Singleton to track the balance."""

    _instance = None

    @staticmethod
    def get_instance():
        return Balance()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._notifier = BalanceNotification() # Not a can of this tight coupling. On the other hand, this is ready for dependency injection as a next step.
        self._balance = 0

    def reset(self):
        """Reset the net balance to zero."""
        self._balance = 0
        return self._balance

    def add_income(self, amount):
        """Add income to the balance."""
        self._balance += amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self._balance -= amount

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        if transaction.category == TransactionCategory.INCOME:
            self._balance += transaction.amount
            self._notifier.notify(self._balance, transaction)
        elif transaction.category == TransactionCategory.EXPENSE:
            self._balance -= transaction.amount
            self._notifier.notify(self._balance, transaction)
        else:
            valid_categories = ", ".join([
                category.value for category in TransactionCategory])
            raise ValueError(
                f"Encountered invalid transaction category. Valid categories are: {valid_categories}.")

    def get_balance(self):
        """Get the current net balance."""
        return self._balance

    def summary(self):
        """Return a summary string of the net balance."""
        pass
    
    def register_observer(self, observer: IBalanceObserver):
        self._notifier.register(observer)


class BalanceNotification:
    """Handles the notifications to balance observers."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._subscribers = []

    def register(self, subscriber: IBalanceObserver):
        self._subscribers.append(subscriber)

    def unregister(self, subscriber: IBalanceObserver):
        self._subscribers.remove(subscriber)
        
    def notify(self, balance, transaction):
        for subscriber in self._subscribers:
            subscriber.update(balance, transaction)
