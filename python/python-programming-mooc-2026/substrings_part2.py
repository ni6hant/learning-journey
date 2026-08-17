inputString = str(input("Please type in a string: "))
length = len(inputString)
count = length

while count >= 0:
    print(inputString[count:length])
    count -= 1