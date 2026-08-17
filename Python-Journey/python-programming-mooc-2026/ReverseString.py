# Write your solution here
inputString = str(input("Please type in a string: "))
lastIndex = len(inputString) - 1
if len(inputString)>0:
    while lastIndex>=0:
        print(inputString[lastIndex])
        lastIndex -= 1

else:
    print("The input string is empty.")