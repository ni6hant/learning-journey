# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
# Write your solution here
def palindromes(checkString:str):
    #lil vs neen
    #-0-1-2 vs +0+1+2+3
    #-3-2-1 vs -4-3-2-1
    for i in range(len(checkString)//2):
        #since we are checking from both ends we only need to check until half for both the odd and even parts
        if checkString[i]!=checkString[-(i+1)]:
            # Immediately return not a string on the first of not matching
            return False
    return True
    
while True:
    checkString = str(input("Please type in a palindrome: "))
    if palindromes(checkString):
        print(f"{checkString} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")