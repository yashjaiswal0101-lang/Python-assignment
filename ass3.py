class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class PayPal:
    def pay(self, amount):
        print("Paid", amount, "using PayPal")


class Payment:
    def __init__(self, method):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)


# Display menu
print("Select Payment Method")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")

choice = int(input("Enter your choice (1-3): "))
amount = float(input("Enter amount: "))

if choice == 1:
    payment = Payment(CreditCard())
elif choice == 2:
    payment = Payment(UPI())
elif choice == 3:
    payment = Payment(PayPal())
else:
    print("Invalid choice!")
    exit()

payment.process(amount)
