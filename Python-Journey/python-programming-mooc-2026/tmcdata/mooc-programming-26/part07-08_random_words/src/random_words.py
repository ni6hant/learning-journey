# Write your solution here
from random import sample

def words(n:int, beginning:str):

    #Store words in a list
    words_list = []
    searched_list = []
    with open("words.txt") as new_file:
        for line in new_file:
            word = line.strip()
            # words_list.append(word)
            if word.startswith(beginning):
                searched_list.append(word)


    #
    return sample(searched_list,n)

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)