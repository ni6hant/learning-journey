# Model solution
# def find_word(str, whatth):
#     index = 0
#     word = ""
#     counter = 0
#     while index < len(str):
#     	if str[index] == " ":
#     	    counter += 1
#     	    if counter == whatth:
#     	        break
#     	    word = ""
#     	else:
#     	    word += str[index]
#     	index += 1
#     return word
 
# def first_word(mjono):
#     return find_word(mjono, 1)
 
# def second_word(mjono):
#     return find_word(mjono, 2)
 
# def last_word(mjono):
#     return find_word(mjono, 0)
# # Write your solution here


# Write your solution here
def first_word(string):
    firstWord = ""
    i=0
    while string[i]!=" " :
        firstWord+=string[i]
        i+=1
        if i>=len(string):
            break
    return firstWord

def second_word(string):
    return first_word(string[len(first_word(string))+1:])

def last_word(string):
    i=len(string)-1
    while string[i]!=" ":
        lastSpaceIndex = i
        i-=1
    return string[lastSpaceIndex:]
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
