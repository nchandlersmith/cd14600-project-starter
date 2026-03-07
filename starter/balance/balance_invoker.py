from balance.balance_commands import BalanceCommand
from transaction.transaction import Transaction

class BalanceInvoker():
    def __init__(self, logger=None):
        self._logger = logger
        self._history = []
    
    def execute(self, command: BalanceCommand):
        self._conditional_log(f"Execute: {command.describe()}")
        command.execute()
        self._history.append(command)
        self._conditional_log(f"Complete: {command.describe()}")
        
    def undo(self):
        if len(self._history) > 0:
            command = self._history.pop()
            self._conditional_log(f"Undo: {command.describe()}")
            self._conditional_log(f"Undo Complete: {command.describe()}")

    def _conditional_log(self, message):
        print("BAM")
        print(message)
        if (self._logger):
            self._logger.log(message)