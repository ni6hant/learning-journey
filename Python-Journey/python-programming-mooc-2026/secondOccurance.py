inputString = str(input("Please type in a string: "))
searchSubString = str(input("Please type in a substring: "))

lengthString = len(inputString)
lengthSearchSubString = len(searchSubString)

# Update: Yes, it does, it is redundant. Tested.
# This might be redundand if the find method has safeguards for such cases
# if lengthSearchSubString > lengthString:
#     print("The search substring should be smaller than the input string.")
# print(inputString.find(searchSubString))

#try to find the first occurance
if inputString.find(searchSubString)!= - 1:
    #if found, cut the substring and the previous characters from the string
    margin = inputString.find(searchSubString) + lengthSearchSubString
    splicedString = inputString[inputString.find(searchSubString)+lengthSearchSubString:]
    #find the string again in the sliced string
    if splicedString.find(searchSubString) != -1 :
        #if found, print the found index of substring+ lenght of the substring
        print(f"The second occurrence of the substring is at index {splicedString.find(searchSubString) + margin}.")
    else :
        #if not found in the spliced string, fial
        print("The substring does not occur twice in the string.")
else:
    #if first occurance not found, don't proceed and fail
    print("The substring does not occur twice in the string.")