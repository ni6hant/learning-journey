# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    func = int(input("Function: "))     

    if func == 3:
        print("Bye!")
        break

    if func == 1:
        #add word
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")

        with open("dictionary.txt", "a") as my_file:
            my_file.write(f"{finnish_word} - {english_word}\n")

        print("Dictionary entry added")

    if func == 2:
        words = []

        search_word = input("Search term: ")
        with open("dictionary.txt") as my_file:
            for line in my_file:
                parts=line.split("-")
                # words.append([parts[0].strip(),parts[1].strip()])
                if search_word in parts[0].strip() or search_word in parts[1].strip():
                    print(line,end="")
        