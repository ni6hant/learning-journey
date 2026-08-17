# Write your solution here
from random import randint, shuffle

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower+1,upper))
    shuffle(number_pool)
    return sorted(number_pool[:amount])

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)