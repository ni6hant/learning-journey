# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if (self.balance-amount)>=0:
            self.balance-=amount
            return True
        return False
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0
        self.regular_lunch_price = 2.50
        self.special_lunch_price = 4.30

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate "change".
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        change_back = payment-self.regular_lunch_price

        if change_back>=0:
            self.funds+=self.regular_lunch_price
            self.lunches+=1
            return change_back
        else:
            return payment

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        change_back = payment-self.special_lunch_price

        if change_back>=0:
            self.funds+=self.special_lunch_price
            self.specials+=1
            return change_back
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        if card.balance-self.regular_lunch_price>=0:
            card.balance-=self.regular_lunch_price
            self.lunches+=1
            return True
        return False

# NB: when paying with a LunchCard the cash funds available at the terminal do not change.
# However, the lunches are still sold whenever there is the required balance available,
# so remember to increase the number of lunches sold appropriately.

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        if card.balance-self.special_lunch_price>=0:
            card.balance-=self.special_lunch_price
            self.specials+=1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        # The card owner pays this by cash, so the deposited sum is added to the funds available at the terminal.
        self.funds += amount
        card.balance+=amount
        pass

if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)