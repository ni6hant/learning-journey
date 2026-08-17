count = 0
sum = 0
mean = 0.0
positiveNumbersCount = 0
negativeNumbersCount = 0


# 0 should not be included in the calcuation. 0 is the breaking character
# there will always be one valid non-zero number


print("Please type in integer numbers. Type in 0 to finish.")

while True:
    inputNumber = int(input("Number: "))
    if inputNumber == 0:
        break
    elif inputNumber > 0:
        positiveNumbersCount += 1
        sum += inputNumber
    elif inputNumber < 0: #else could have work but this makes it a better readable code
        negativeNumbersCount += 1
        sum += inputNumber



count = positiveNumbersCount + negativeNumbersCount
mean = sum/count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positiveNumbersCount}")
print(f"Negative numbers {negativeNumbersCount}")