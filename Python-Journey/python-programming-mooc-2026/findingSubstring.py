inputString = str(input("Please type in a word: "))
searchCharacter = str(input("Please type in a character: "))

length = len(inputString)
foundIndex = inputString.find(searchCharacter)

if foundIndex != -1 and (foundIndex+3) <= length:
    #Only process if the search character even exists, AND
    #The found index is atleast three places from the end
    print(inputString[foundIndex:foundIndex+3])

