# Write your solution to exercise 2 here
def find_allowed(word_list:list,minimum:int):
    searchString = "aeiouy"
    new_list =[]
    
    for word in word_list:
        count = 0
        for char in searchString:
            count+=word.count(char)
        if count>=minimum:
            new_list.append(word)
            
    return new_list

if __name__ == "__main__":
    word_list = ["apple","banana","cherry","orange", "peach", "pineapple"]
    minimum = 3
    print(find_allowed(word_list,minimum))