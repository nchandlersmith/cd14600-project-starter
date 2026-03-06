from balance.balance_commands import BalanceCommand
from transaction.transaction import Transaction

class BalanceInvoker():
    def __init__(self, logger=None):
        self._logger = logger
    
    def execute(self, command: BalanceCommand):
        self._conditional_log(f"Execute: {command.describe()}")
        command.execute()

    def _conditional_log(self, message):
        print(message)
        print(self._logger)
        self._logger.log(message)