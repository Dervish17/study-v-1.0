from abc import ABC, abstractmethod


class Transaction:
    def __init__(self, currency):
        self.currency = currency

    def execute(self):
        return (f"Абстракция: Базовая операция через:\n"
                f"{self.currency.convert_amount()}")


class BankTransfer(Transaction):
    def execute(self):
        return (f"Банковский перевод:\n"
                f"{self.currency.convert_amount()}")


class MobileAppTransfer(Transaction):
    def execute(self):
        return (f"Мобильный перевод:\n"
                f"{self.currency.convert_amount()}")


class Currency(ABC):
    @abstractmethod
    def convert_amount(self):
        pass


class USD(Currency):

    def convert_amount(self):
        return 'Перевод произведен в Долларах'


class EUR(Currency):
    def convert_amount(self):
        return 'Перевод произведен в Евро'


def client_code(transaction):
    print(transaction.execute(), end='\n')


currency = USD()
transaction = MobileAppTransfer(currency)
client_code(transaction)
print()
currency = EUR()
transaction = BankTransfer(currency)
client_code(transaction)
