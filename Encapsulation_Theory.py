What is Encapsulation?

Binding data and methods together and hiding sensitive data from outside access.

👉 Achieved using private variables.

Example:
class BankAccount:
    def __init__(self):
        self.__balance = 1000   # private variable

    def show_balance(self):
        print(self.__balance)

obj = BankAccount()
obj.show_balance()


❌ This will give error:

print(obj.__balance)


📌 __balance cannot be accessed directly
