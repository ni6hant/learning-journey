

inputString = str(input("Please type in a word: "))
searchCharacter = str(input("Please type in a character: "))

while True:    
    if inputString.find(searchCharacter) != -1 and (inputString.find(searchCharacter)+3) <= len(inputString):
        #Only process if the search character even exists, AND
        #The found index is atleast three places from the end
        print(inputString[inputString.find(searchCharacter):inputString.find(searchCharacter)+3])

        inputString = inputString[inputString.find(searchCharacter)+1:]
    else:
        break
    
    
