# Write your solution here
from string import ascii_lowercase

def store_words(filename):
    words_list = []
    with open(filename) as my_file:
        for line in my_file:
            words_list.append(line.strip())
    return words_list

def find_words(search_term:str):
    found_words = []
    words = store_words("words.txt")

    # If there are no wildcard characters in the search term, only words which match the search term exactly are returned.
    if "." not in search_term and "*" not in search_term:
        found_words.append(search_term)

    # A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield words like ping and pong, and .a.e would yield words like sane, care and late.
    if "." in search_term:
        filtered_search = []

        # First filteration is based on the length as this is . search and we know the exact length
        for word in words:
            if len(word) == len(search_term):
                filtered_search.append(word)

        for word in filtered_search:
            flag = True
            for i in range(0,len(search_term)):
                if search_term[i]!="." and flag:
                    if word[i] != search_term[i]:
                        flag = False
                    else:
                        flag = True
            if flag:
                found_words.append(word)


    # An asterisk * at the end of the search term means that any word which begins with the search term is acceptable. An asterisk at the beginning of the search term means that any word which ends with the search term is acceptable. For example, ca* would yield words like california, cat, caring and catapult, while *ane would yield words like crane, insane and aeroplane. There can only ever be a single asterisk in the search term.
    if "*" in search_term:
        parts = search_term.split("*")

        filtered_search = words

        for word in filtered_search:
            #  * at the beginning
            if parts[0] == "":
                if word.endswith(parts[1]):
                    found_words.append(word)

            # * at the end
            if parts[1] == "":
                if word.startswith(parts[0]):
                    found_words.append(word)
        
    return found_words

if __name__ == "__main__":
    print(find_words("*okes"))
    print(find_words("reson*"))