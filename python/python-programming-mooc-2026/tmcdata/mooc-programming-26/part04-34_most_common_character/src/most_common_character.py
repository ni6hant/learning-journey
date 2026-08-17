# Write your solution here
def most_common_character(my_string:str):
    count=0
    for char in my_string:
        current_count = my_string.count(char)
        if current_count>count:
            count=current_count
            common_character=char
    return common_character

if __name__ == "__main__":
    most_common_character("aaabb")