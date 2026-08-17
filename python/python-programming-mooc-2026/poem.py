# Write your solution here
poem = ""
previousWord = ""

while True:    
    inputWord = str(input("Please type in a word: "))
    if inputWord == previousWord or inputWord == "end":
        break
    else:
        poem= poem + " " + inputWord
        previousWord = inputWord



print(poem)