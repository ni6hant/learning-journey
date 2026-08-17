# Write your solution here
import string

def separate_characters(my_string:str):
    lower_and_upper=""
    punctuation=""
    all_other_incl_whitespace=""

    for char in my_string:
        if char in string.ascii_letters:
            lower_and_upper+=char
        elif char in string.punctuation:
            punctuation+=char
        else:
            all_other_incl_whitespace+=char
    separate_characters_string = (lower_and_upper, punctuation, all_other_incl_whitespace)
    return separate_characters_string

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])