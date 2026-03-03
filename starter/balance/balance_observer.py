# balance_observer.py

class IBalanceObserver:
    def update(self, balance, transaction):
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    def __init__(self):
        super().__init__()
        self._latest_message = ""

    @property
    def latest_message(self):
        return self._latest_message

    def update(self, balance, transaction):
        """Print balance update message."""
        message = f"Transaction posted: ${transaction.amount} {transaction.category.value.upper()}. New balance: ${balance}."
        self._latest_message = message
        print(message)


class LowBalanceAlertObserver(IBalanceObserver):
    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def update(self, balance, transaction):
        """Alert if balance drops below threshold."""
        self.alert_triggered = balance < self.threshold
