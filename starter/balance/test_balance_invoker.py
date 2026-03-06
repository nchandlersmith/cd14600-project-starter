from balance.balance_invoker import BalanceInvoker

import unittest
from unittest.mock import Mock

class TestBalanceInvoker(unittest.TestCase):
    def test_execute_executes_a_command(self):
        command = Mock()
        command.execute.return_value = None
        invoker = BalanceInvoker()
        
        invoker.execute(command)
        
        command.execute.assert_called_once()
        