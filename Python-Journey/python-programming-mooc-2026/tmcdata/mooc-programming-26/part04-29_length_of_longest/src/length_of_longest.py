# Write your solution here
def length_of_longest(listOfStrings:str):
    lengthOfLongestString = 0
    for item in listOfStrings:
        if len(item)>lengthOfLongestString:
            lengthOfLongestString=len(item)
    return lengthOfLongestString

if __name__ == "__main__":
    length_of_longest(["first", "second", "fourth", "eleventh"])