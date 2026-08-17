# Write your solution here:
class LunchCard:
    lunch_price = 2.60
    special_price = 4.60

    def __str__(self):
        return f"The balance is {self.balance:0.1f} euros"

    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:0.1f} euros"
    
    def eat_lunch(self):
        if (self.balance-self.lunch_price)>0:
            self.balance -= self.lunch_price

    def eat_special(self):
        if (self.balance-self.special_price)>0:
            self.balance -= self.special_price

    def deposit_money(self,amount:int):
        if amount<0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount


peters_card = LunchCard(20)
graces_card = LunchCard(30)

peters_card.eat_special()
graces_card.eat_lunch()
print("Peter: "+str(peters_card))
print("Grace: "+str(graces_card))

peters_card.deposit_money(20)
graces_card.eat_special()
print("Peter: "+str(peters_card))
print("Grace: "+str(graces_card))

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print("Peter: "+str(peters_card))
print("Grace: "+str(graces_card))
