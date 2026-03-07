from balance.balance_invoker import BalanceInvoker
from balance.balance_commands import ApplyTransaction, AddIncome
from transaction.transaction_category import TransactionCategory
from transaction.transaction import Transaction
from balance.balance import Balance

import unittest
from unittest.mock import Mock, call


class TestBalanceInvoker(unittest.TestCase):
    def test_execute_executes_a_command(self):
        command = Mock()
        command.execute.return_value = None
        invoker = BalanceInvoker()

        invoker.execute(command)

        command.execute.assert_called_once()

    def test_execute_logs_execution(self):
        logger = Mock()
        invoker = BalanceInvoker(logger)
        command = ApplyTransaction(Balance(), Transaction(
            135, TransactionCategory.EXPENSE))

        invoker.execute(command)

        assert logger.log.call_count == 2
        print(logger.log.call_args_list)
        assert logger.log.call_args_list == [
            call("Execute: Apply transaction: $135 EXPENSE."),
            call("Complete: Apply transaction: $135 EXPENSE.")
        ]

    def test_undo_is_safe_no_previous_operation(self):
        command = Mock()
        logger = Mock()
        invoker = BalanceInvoker(logger)

        invoker.undo()

        command.assert_not_called()
        logger.assert_not_called()
        
    def test_undo_undoes_previous_operation(self):
        command = Mock()
        invoker = BalanceInvoker()
        invoker.execute(command)
        
        invoker.undo()
        
        self.assertEqual(command.undo.call_count, 1)
        command.undo.assert_called_with(command)

    def test_execute_logs_undo(self):
        logger = Mock()
        invoker = BalanceInvoker(logger)
        transaction = ApplyTransaction(Balance(), Transaction(
            135, TransactionCategory.EXPENSE))
        income = AddIncome(Balance(), 100)
        invoker.execute(transaction)
        invoker.execute(income)

        invoker.undo()

        assert logger.log.call_count == 6
        print("test")
        print(logger.log.call_args_list)
        assert logger.log.call_args_list == [
            call("Execute: Apply transaction: $135 EXPENSE."),
            call("Complete: Apply transaction: $135 EXPENSE."),
            call("Execute: Add income: $100."),
            call("Complete: Add income: $100."),
            call("Undo: Add income: $100."),
            call("Undo Complete: Add income: $100.")
        ]
