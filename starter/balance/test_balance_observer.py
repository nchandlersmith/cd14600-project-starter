import unittest
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from balance.balance import Balance, BalanceNotification
from balance.balance_observer import LowBalanceAlertObserver


class TestLowBalanceAlertObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_alert_triggers_on_low_balance(self):
        observer = LowBalanceAlertObserver(threshold=50)
        self.balance.register_observer(observer)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME))
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE))
        self.assertTrue(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME))
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE))
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE))
        self.assertTrue(observer.alert_triggered)

    def test_balance_notification_initilizes_with_0_subscriptions(self):

        notifier = BalanceNotification()
        self.assertEqual(len(notifier._subscribers), 0)

    def test_balance_notification_adds_a_subscriber(self):
        notifier = BalanceNotification()
        subscriber = LowBalanceAlertObserver(threshold=9001)
        notifier.register(subscriber)
        self.assertEqual(len(notifier._subscribers), 1)
        self.assertIs(notifier._subscribers[0], subscriber)

    def test_balance_notification_removes_a_subscriber(self):
        notifier = BalanceNotification()
        subscriber = LowBalanceAlertObserver(threshold=3)
        notifier.register(subscriber)
        notifier.unregister(subscriber)
        self.assertEqual(len(notifier._subscribers), 0)

    def test_balance_notification_removes_the_correct_subscriber(self):
        notifier = BalanceNotification()
        subscriber1 = LowBalanceAlertObserver(threshold=3)
        subscriber2 = LowBalanceAlertObserver(threshold=10)
        notifier.register(subscriber1)
        notifier.register(subscriber2)
        notifier.unregister(subscriber1)
        self.assertEqual(len(notifier._subscribers), 1)
        self.assertEqual(notifier._subscribers[0], subscriber2)


if __name__ == "__main__":
    unittest.main()
