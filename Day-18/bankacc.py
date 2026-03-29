from abc import ABC,abstractmethod  #ABC=Abstract Base Class
class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingAccount(BankAccount):
    def deposit(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakh you can withdraw")
        
class CurrentAccount(BankAccount):
    def deposit(self):
        print("unlimited deposit")
    def withdraw(self):
        print("unlimited withdraw")
        
class JointAccount(BankAccount):
    def deposit(self):
        print("only those 2 people can deposit")
    def withdraw(self):
        print("1-2 lakhs per day you can withdraw")
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("no limit")
    def withdraw(self):
        print("20t-1L per day")
        
class PensionAccount(BankAccount):
    def deposit(self):
        print("no deposit")
    def withdraw(self):
        print("40t per day")
        
print("---abhinandhan---")
abhinandhan= SavingAccount()
abhinandhan.checkbalance()
abhinandhan.deposit()
abhinandhan.withdraw()

print("---praveen---")
praveen=CurrentAccount()
praveen.checkbalance()
praveen.deposit()
praveen.withdraw()

print("---saaketh_nikhil---")
saaketh_nikhil=JointAccount()
saaketh_nikhil.checkbalance()
saaketh_nikhil.deposit()
saaketh_nikhil.withdraw()

print("---shanmukh---")
shanmukh=SalaryAccount()
shanmukh.checkbalance()
shanmukh.deposit()
shanmukh.withdraw()

print("---swapnil---")
swapnil=PensionAccount()
swapnil.checkbalance()
swapnil.deposit()
swapnil.withdraw()
