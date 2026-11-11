from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print("Credit Card Payment:", amount, "processed successfully")
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print("PayPal Payment:", amount, "processed successfully")
class UPIProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print("UPI Payment:", amount, "processed successfully")
p1 = CreditCardProcessor()
p2 = PayPalProcessor()
p3 = UPIProcessor()
processors = [p1, p2, p3]
amount = 1500
for processor in processors:
    processor.process_payment(amount)