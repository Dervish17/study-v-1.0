from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self):
        print("Платеж с помощью кредитной карты успешно проведен.")


class EWalletPayment(PaymentStrategy):
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"Платеж с помощью электронного кошелька успешно проведен, в размере {self.amount} денежных единиц")


class CashPayment(PaymentStrategy):
    def __init__(self, cash_amount):
        self.cash_amount = cash_amount

    def pay(self):
        print(f"Платеж наличными успешно проведен, в размере {self.cash_amount} денежных единиц")


class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def make_payment(self):
        if isinstance(self.payment_strategy, CreditCardPayment):
            self.payment_strategy.pay()
        elif isinstance(self.payment_strategy, EWalletPayment):
            self.payment_strategy.pay()
        elif isinstance(self.payment_strategy, CashPayment):
            self.payment_strategy.pay()
        else:
            print("Неподдерживаемая стратегия оплаты")

    def set_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy


def main():
    context = PaymentContext(CreditCardPayment('1234567890'))
    context.make_payment()
    context.set_strategy(EWalletPayment(100))
    context.make_payment()


if __name__ == "__main__":
    main()
