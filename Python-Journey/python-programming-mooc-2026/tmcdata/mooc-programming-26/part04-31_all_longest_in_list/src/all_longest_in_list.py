# Write your solution here
def length_of_longest(listOfStrings:str):
    lengthOfLongestString = 0
    for item in listOfStrings:
        if len(item)>lengthOfLongestString:
            lengthOfLongestString=len(item)
    return lengthOfLongestString


def all_the_longest(my_list:list):
    longestLength = length_of_longest(my_list)
    longestList =[]
    for item in my_list:
        if len(item)==longestLength:
            longestList.append(item)
    return longestList

if __name__ == "__main__":
    all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])