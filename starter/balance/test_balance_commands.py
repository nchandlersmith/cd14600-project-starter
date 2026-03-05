"""Doing an integration style testing here of the underlying functionality.
I could using mocking to test that the command calls the balance, 
but that is testing the implementation; I want to avoid that."""

from balance.balance import Balance
from balance.balance_commands import ResetBalance

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
        
