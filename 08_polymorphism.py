class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement pay()")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} through UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using Credit/Debit Card")

class PayPal(Payment):
    pass
    # def pay(self, amount):
    #     print(f"Paying ₹{amount} via PayPal")

def process_payment(payment_method: Payment, amount):
    payment_method.pay(amount)

# Different objects, SAME function call
process_payment(UPI(), 500)
process_payment(Card(), 500)

paying = PayPal()

# If you never call the missing method → no error ever happens

# The class can still be instantiated

# Bugs appear later, sometimes deep in the code

# That's the differrence between Abstraction and Polymorphism