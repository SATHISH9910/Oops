# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"₹{amount} deposited successfully.")
#         else:
#             print("Deposit amount must be greater than 0.")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"₹{amount} withdrawn successfully.")
#         else:
#             print("Insufficient balance.")

#     def check_balance(self):
#         print(f"Current Balance: ₹{self.__balance}")


# # Create an object
# b = Bank(300000)

# # Check initial balance
# b.check_balance()

# # Deposit money
# b.deposit(5000)
# b.check_balance()

# # Withdraw money
# b.withdraw(10000)
# b.check_balance()

# # Try withdrawing more than the available balance
# b.withdraw(500000)
# b.check_balance()


# class Bank:
#     def __init__(self,balance):
#         self.__balance= balance
    
    # def deposit(self,amount):
    #     if amount > 0:
    #         self.__balance += amount
    #         print(f"{amount} deposite successfully")
    #     else:
    #         print("Deposit amount must be greater than 0")
    
    # def withdraw(self,amount):
    #     if amount <=self.__balance:
    #         self.__balance -= amount
    #         print(f"{amount} Withdrawn successfully")
    #     else:
    #         print("Insufficient balance")

    # def check_balance(self):
    #      print(f"Current Balance: {self.__balance}")

# b=Bank(10000)
# b.check_balance()
# b.deposit(0)
# b.check_balance()
# b.withdraw(24000)
# b.check_balance()

     
class Bank():
    def __init__(self,account_holder,account_number,Ifsc_code,balance):
        self.account_number= account_number
        self.account_holder = account_holder
        self.Ifsc_code = Ifsc_code
        self.__balance= balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposite successfully")
        else:
            print("Deposit amount must be greater than 0")
    
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance -= amount
            print(f"{amount} Withdrawn successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("\n ------Account details ---------")
        print(f"Account Holder:{self.account_holder}")
        print(f"Account No: {self.account_number}")
        print(f"Ifsc code : {self.Ifsc_code}")
        print(f"Current Balance: {self.__balance}")
        print("-----------------------------")

b= Bank('Sathish','843434483299','GIJJJ23453',3030339388848)
b.deposit(45454355)
b.check_balance()
b.withdraw(404040)
b.check_balance()
    
