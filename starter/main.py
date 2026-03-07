"""This module serves as the entry point for the program."""
from balance.balance import Balance
from balance.balance_commands import ApplyTransaction
from balance.balance_invoker import BalanceInvoker
from balance.balance_observer import LowBalanceAlertObserver
from balance.balance_observer import PrintObserver
from logger.logger import Logger
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_adapter import TransactionAdapter
from transaction.external_income_transaction import ExternalFreelanceIncome


def main():
    print("Adding transactions...")

    # Create balance & add observers
    balance = Balance.get_instance()
    balance.register_observer(PrintObserver())
    balance.register_observer(LowBalanceAlertObserver(threshold=100))

    # Create standard transactions
    transactions = [
        Transaction(100, TransactionCategory.INCOME),
        Transaction(50, TransactionCategory.EXPENSE),
        Transaction(200, TransactionCategory.INCOME),
        Transaction(75, TransactionCategory.EXPENSE),
    ]

    # Create an external income transaction (via Adapter pattern)
    freelance_income = ExternalFreelanceIncome(
        1200, "INV-98765", "Mobile App Project")
    adapter = TransactionAdapter(freelance_income)
    adapted_transaction = adapter.to_transaction()

    all_transactions = transactions + [adapted_transaction]

    # Apply all transactions to balance
    for transaction in all_transactions:
        balance.apply_transaction(transaction)

    print("\nUsing command pattern...")
    invoker = BalanceInvoker(Logger())
    transaction1 = ApplyTransaction(balance, Transaction(3400, TransactionCategory.INCOME))
    transaction2 = ApplyTransaction(balance, Transaction(78.41, TransactionCategory.EXPENSE))
    transaction3 = ApplyTransaction(balance, Transaction(1078.41, TransactionCategory.EXPENSE))
    invoker.execute(transaction1)
    invoker.execute(transaction2)
    invoker.undo()
    invoker.execute(transaction3)
    
    


if __name__ == "__main__":
    main()
