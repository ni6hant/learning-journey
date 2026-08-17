# Write your solution here

def longest(string_list:list):
    longest_string = ""
    for item in string_list:
        if len(item)>len(longest_string):
            longest_string = item
    return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))