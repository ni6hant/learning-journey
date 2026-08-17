# Write your solution here
import string

def change_case_per_character(c:str):
    if c==" ":
        return " "

    lower = string.ascii_lowercase #'abcdefghijklmnopqrstuvwxyz'
    upper = string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    find_in_lower = lower.find(c)
    find_in_upper = upper.find(c)

    if find_in_lower !=- 1:
        return upper[find_in_lower]
    if find_in_upper != -1:
        return lower[find_in_upper]

def change_case(orig:str):
    new_str = ""
    for char in orig:
        new_str+=change_case_per_character(char)
    return new_str

def split_in_half(orig_string: str):
    first_half = orig_string[:(len(orig_string)//2)]
    second_half = orig_string[(len(orig_string)//2):]
    return (first_half,second_half)

def remove_special_characters(orig_string: str):
    non_special = string.ascii_letters+string.digits+" "
    new_str = ""
    for char in orig_string:
        if char in non_special:
            new_str += char
    return new_str

if __name__ == "__main__":
    print(change_case('TWO DIFFERENT WORDS'))