# class Employee():
#     def __init__(self,name,employee_id,salary):
#         self.name=name
#         self.employee_id=employee_id
#         self.salary=salary
#     def display_details(self):
#         print(f"name: {self.name}")
#         print(f"employee_id: {self.employee_id}")
#         print(f"salary: {self.salary}")
#         print("-" * 30)
#     def increment_salary(self,amount):
#         self.salary += amount
#         print(f"salary increased by {amount}")


# e=Employee("Sathish","BNJJ7772",50000)
# e.increment_salary(49535)
# e.display_details()
# e1=Employee("adesh","JSDFSJDF33",959453)
# e1.increment_salary(111235)
# e1.display_details()
# e2=Employee("vignesh","SJDFSJDF44",39393)
# e2.increment_salary(454235)
# e2.display_details() 


class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance}")


# Create an object
b = Bank(300000)

# Check initial balance
b.check_balance()

# Deposit money
b.deposit(5000)
b.check_balance()

# Withdraw money
b.withdraw(10000)
b.check_balance()

# Try withdrawing more than the available balance
b.withdraw(500000)
b.check_balance()