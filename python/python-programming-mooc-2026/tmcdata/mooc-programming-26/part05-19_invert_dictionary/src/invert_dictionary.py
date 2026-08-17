# Write your solution here
def invert(dictionary_s:dict):
    new_dictionary = {}
    for key,value in dictionary_s.items():
        new_dictionary[value] = key
    dictionary_s.clear()
    for key,value in new_dictionary.items():
        dictionary_s[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)