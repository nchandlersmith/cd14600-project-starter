from balance.balance_invoker import BalanceInvoker
from balance.balance_commands import ApplyTransaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction import Transaction
from balance.balance import Balance

import unittest
from unittest.mock import Mock

class TestBalanceInvoker(unittest.TestCase):
    def test_execute_executes_a_command(self):
        command = Mock()
        command.execute.return_value = None
        invoker = BalanceInvoker()
        
        invoker.execute(command)
        
        command.execute.assert_called_once()
        
    def test_execute_logs_before_execution(self):
        logger = Mock()
        invoker = BalanceInvoker(logger)
        command = ApplyTransaction(Balance())
        transaction = Transaction(135, TransactionCategory.EXPENSE)
        
        invoker.execute(command, transaction)
        
        logger.log.assert_called_once()
        