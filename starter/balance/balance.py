# balance.py

from transaction.transaction_category import TransactionCategory

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
        self._balance = 0

    def reset(self):
        """Reset the net balance to zero."""
        pass

    def add_income(self, amount):
        """Add income to the balance."""
        pass

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        pass

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        pass

    def get_balance(self):
        """Get the current net balance."""
        return self._balance

    def summary(self):
        """Return a summary string of the net balance."""
        pass
    
