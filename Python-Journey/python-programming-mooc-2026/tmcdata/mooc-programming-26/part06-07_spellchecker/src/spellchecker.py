# write your solution here

text = input("Write text")
# text = "This is acually a good and usefull program"

words = text.split(" ")
correct_words = []

with open("wordlist.txt") as new_file:
    for correct_word in new_file:
        correct_words.append(correct_word.strip().lower())

for word in words: 
    if word.lower() in correct_words:
        print(word,end=" ")
    else:
        print(f'*{word}*',end=" ")