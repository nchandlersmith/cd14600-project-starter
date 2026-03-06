from balance.balance_commands import BalanceCommand

class BalanceInvoker():
    def __init__(self):
        pass
    
    def execute(self, command: BalanceCommand):
        command.execute()