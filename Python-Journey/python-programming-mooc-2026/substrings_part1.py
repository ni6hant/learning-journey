inputString = str(input("Please type in a string: "))
length = len(inputString)
count = 1

while count <= length:
    print(inputString[0:count])
    count += 1