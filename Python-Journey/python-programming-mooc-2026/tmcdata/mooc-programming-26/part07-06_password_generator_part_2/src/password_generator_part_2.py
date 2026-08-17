# Write your solution here
from random import randint, shuffle, choice
from string import ascii_lowercase, digits

def generate_strong_password(max_length,one_or_more_numbers:bool,one_or_more_special_characters:bool):
    password = ""

    if one_or_more_numbers:
        number_of_numbers = randint(1,max_length-2)
        for i in range(0,number_of_numbers):
            password += choice(digits)
    else:
        number_of_numbers = 0

    special_characters = "!?=+-()#"
    if one_or_more_special_characters:
        number_of_special_characters = randint(1,max_length-number_of_numbers-1)
        for i in range(0,number_of_special_characters):
            password+= choice(special_characters)#-1 as randint is []
    else:
        number_of_special_characters = 0

    #Special case if there is no space left for the ascii lower case.
    # if max_length-number_of_numbers-number_of_special_characters==0:
    #     if number_of_special_characters>=number_of_numbers:
    #         number_of_special_characters-=1
    #     else:
    #         number_of_numbers-=1

    for i in range(0,max_length-number_of_numbers-number_of_special_characters):
        password+=choice(ascii_lowercase)

    shuffled = []
    for char in password:
        shuffled.append(char)
    shuffle(shuffled)

    password = ""
    for char in shuffled:
        password+=char
    return password

if __name__ == "__main__":
    print(generate_strong_password(5,True,True))