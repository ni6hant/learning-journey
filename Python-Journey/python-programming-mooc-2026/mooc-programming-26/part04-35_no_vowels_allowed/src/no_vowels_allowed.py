# Write your solution here
def no_vowels(my_string:str):
    # new_string = ""
    new_string = my_string.replace("a","")
    new_string = new_string.replace("e","")
    new_string = new_string.replace("i","")
    new_string = new_string.replace("o","")
    new_string = new_string.replace("u","")
    # for char in my_string:
    #     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    return new_string

if __name__ == "__main__":
    no_vowels("this is an example")