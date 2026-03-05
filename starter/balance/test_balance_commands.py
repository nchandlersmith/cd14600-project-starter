"""Doing an integration style testing here of the underlying functionality.
I could using mocking to test that the command calls the balance, 
but that is testing the implementation; I want to avoid that."""

from balance.balance import Balance
from balance.balance_commands import AddIncome

import unittest


class TestBalanceCommand(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_add_income_command_adds_income(self):
        add_income = AddIncome(self.balance)

        add_income.execute(800)

        self.assertEqual(self.balance._balance, 800)

    def test_undo_add_income_removes_last_income_from_balance(self):
        add_income = AddIncome(self.balance)
        add_income.execute(125)
        add_income.execute(80)

        add_income.undo()
        add_income.undo()

        self.assertEqual(self.balance._balance, 0)
