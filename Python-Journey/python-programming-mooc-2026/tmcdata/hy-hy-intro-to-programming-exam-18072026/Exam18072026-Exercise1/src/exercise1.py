# Write your solution to exercise 1 here
def most_common_character(combinedString:str):
    count = 0
    most_repeated = ""
    for char in combinedString:
        if combinedString.count(char)>count: #count the current character in the string
            most_repeated = char #if the count is more than the previous count, store the new character
            count = combinedString.count(char)
    return most_repeated


count = 0
lengthOfLongestString = 0
combinedString = ""

while True:
    input_string = input("Type in a string: ")
    if input_string == "":
        break

    #Count the total number of strings
    count+=1

    #Store the longest String
    if lengthOfLongestString<len(input_string):
        lengthOfLongestString=len(input_string)

    #Store all the string as one large string for testing later
    combinedString+=input_string

mostCommonCharacter = most_common_character(combinedString)

print(f"Total number of strings: {count}")
print(f"The length of the longest string: {lengthOfLongestString}")
print(f"The most common character in strings: {mostCommonCharacter}")