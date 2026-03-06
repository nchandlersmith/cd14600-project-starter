"""Doing an integration style testing here of the underlying functionality.
I could using mocking to test that the command calls the balance, 
but that is testing the implementation; I want to avoid that."""

from balance.balance import Balance
from balance.balance_commands import AddIncome, AddExpense, ApplyTransaction, GetBalance
from transaction.transaction import Transaction, TransactionCategory

import unittest


class TestBalanceCommand(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_add_income_command_adds_income(self):
        add_income = AddIncome(self.balance)
        add_income.execute(800)
        self.assertEqual(self.balance._balance, 800)

    def test_add_income_undo_command_removes_income(self):
        add_income = AddIncome(self.balance)
        add_income.execute(100)

        add_income.undo()

        self.assertEqual(self.balance._balance, 0)

    def test_undo_add_income_removes_last_income_from_balance(self):
        add_income = AddIncome(self.balance)
        add_income.execute(125)
        add_income.execute(80)

        add_income.undo()
        add_income.undo()

        self.assertEqual(self.balance._balance, 0)

    def test_add_expense_command_adds_expense(self):
        add_expense = AddExpense(self.balance)
        add_expense.execute(100)
        self.assertEqual(self.balance._balance, -100)

    def test_add_expense_undo_undoes(self):
        add_expense = AddExpense(self.balance)
        add_expense.execute(50)

        add_expense.undo()

        self.assertEqual(self.balance._balance, 0)

    def test_undo_add_income_removes_last_income_from_balance(self):
        add_expense = AddExpense(self.balance)
        add_expense.execute(125)
        add_expense.execute(80)

        add_expense.undo()
        add_expense.undo()

        self.assertEqual(self.balance._balance, 0)

    def test_apply_transaction_execute_applies_income_transaction(self):
        apply = ApplyTransaction(self.balance)

        apply.execute(Transaction(2500.67, TransactionCategory.INCOME))

        self.assertEqual(self.balance._balance, 2500.67)

    def test_apply_transaction_undo_undoes_income_transaction(self):
        apply = ApplyTransaction(self.balance)
        apply.execute(Transaction(2500.67, TransactionCategory.INCOME))

        apply.undo()

        self.assertEqual(self.balance._balance, 0)

    def test_apply_transaction_undo_undoes_last_income_transaction(self):
        apply = ApplyTransaction(self.balance)
        apply.execute(Transaction(2000, TransactionCategory.INCOME))
        apply.execute(Transaction(500, TransactionCategory.EXPENSE))

        apply.undo()

        self.assertEqual(self.balance._balance, 2000)
        
    def test_get_balance_get_the_balance(self):
        get_balance = GetBalance(self.balance)
        self.balance._balance = 67
        balance = get_balance.execute()
        self.assertEqual(balance, 67)
