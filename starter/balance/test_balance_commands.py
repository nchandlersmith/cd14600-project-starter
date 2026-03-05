"""Doing an integration style testing here of the underlying functionality.
I could using mocking to test that the command calls the balance, 
but that is testing the implementation; I want to avoid that."""

from balance.balance import Balance
from balance.balance_commands import ResetBalance, AddIncome

import unittest


class TestBalanceCommand(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_reset_command_sets_balance_to_zero(self):
        self.balance.add_income(1200)
        reset = ResetBalance(self.balance)
        
        reset.execute()
        
        self.assertEqual(self.balance._balance, 0)
        
    def test_undo_reset_command_applies_previous_balance(self):
        self.balance.add_income(500)
        reset = ResetBalance(self.balance)
        reset.execute()
        
        reset.undo()
        
        self.assertEqual(self.balance._balance, 500)
        

    def test_add_income_command_adds_income(self):
        add_income = AddIncome(self.balance)
        
        add_income.execute(800)
        
        self.assertEqual(self.balance._balance, 800)
        