# Write your solution here
def shortest(listOfStrings:str):
    shortestString = listOfStrings[0]
    for item in listOfStrings:
        if len(item)<len(shortestString):
            shortestString=item
    return shortestString

if __name__ == "__main__":
    shortest(["first", "second", "fourth", "eleventh"])