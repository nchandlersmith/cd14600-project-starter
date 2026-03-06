from balance.balance_commands import BalanceCommand
from transaction.transaction import Transaction

class BalanceInvoker():
    def __init__(self, logger=None):
        self._logger = logger
    
    def execute(self, command: BalanceCommand, *args):
        self._conditional_log()
        command.execute(*args)

    def _conditional_log(self):
        if self._logger is not None:
            self._logger.log()