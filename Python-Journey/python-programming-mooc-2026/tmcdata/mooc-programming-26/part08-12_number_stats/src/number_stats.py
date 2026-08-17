# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.sum = 0
        self.even_count = 0
        self.odd_count = 0
        self.even_sum = 0
        self.odd_sum = 0

    def add_number(self, number:int):
        self.numbers+=number
        self.count +=1
        self.sum += number
        if number%2==0:
            self.even_count+=1
            self.even_sum+=number
        else:
            self.odd_count+=1
            self.odd_sum+=number

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.sum

    def average(self):
        if self.count == 0:
            return 0
        return self.sum/self.count


stats = NumberStats()
while True:
    try:
        number = int(input("Please type in integer numbers:"))
    except:
        print("Please input an integer.")
    if number == -1:
        break
    stats.add_number(number)
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:",stats.even_sum)
print("Sum of odd numbers:",stats.odd_sum)