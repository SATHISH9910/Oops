class Payment:
    def pay(self):
        print("Payment successfull")
                                              #A common parent class contains the method that will be overridden.#
class Upi(Payment):
    def pay(self):
        print("Paid ₹500 using UPI")

class DebitCard(Payment):                       # child class musr inherit the parent class
    def Pay(self):
        print("Paid ₹500 using Debitcard")

class Creditcard(Payment):
    def Pay(self):         #same method name#
        print("Paid ₹500 using CrediCArd")

class NEtBanking(Payment):
    def pay(self):
        print("Paid ₹500 using NetBanking")     # but different Implementations#

P=Payment()                                                                                    #   > Create Objects of Child Classes#
Payments=[Upi(),DebitCard(),Creditcard(),NEtBanking()]   #"" #
for Payment in Payments:
    Payment.pay()            # call the same method #  