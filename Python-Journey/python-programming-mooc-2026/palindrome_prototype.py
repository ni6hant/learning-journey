inputString = str(input("Please type in a string: "))

if len(inputString)>1:
    if inputString[1]==inputString[-2]:
        print(f"The second and the second to last characters are {inputString[1]}")
    else:
        print("The second and the second to last characters are different")

else:
    print("The input string is empty.")


