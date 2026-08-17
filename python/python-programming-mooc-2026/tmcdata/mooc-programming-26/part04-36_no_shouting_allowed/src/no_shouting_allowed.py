# Write your solution here
def no_shouting(my_list:list):
    new_list=[]
    for item in my_list:
        if item.isupper():
            continue
        else:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"])