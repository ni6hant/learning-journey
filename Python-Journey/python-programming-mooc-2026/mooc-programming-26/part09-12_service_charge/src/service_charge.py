# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self,owner:str, account_number:str, balance:float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount: float):
        if amount>0:
            self.__balance+=amount
            self.__service_charge()
        else:
            raise ValueError("Amount depositing has to be more than zero.")

    def withdraw(self,amount: float):
        if amount>0:
            self.__balance-=amount
            self.__service_charge()
        else:
            raise ValueError("Amount depositing has to be more than zero.")

    def __service_charge(self):
        self.__balance = self.__balance*(1 - 1/100)