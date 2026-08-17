sentence = str(input("Please type in a sentence: "))

i=0

#if length of sentence > 0 : 
if len(sentence) > 0:
    #print the first character
    print(sentence[0])

    # loop through each character of the string until a space is found 
    # break if index>length of string
    # when space is found
    while (i+1)<len(sentence):
        if sentence[i]==" " and sentence[i+1] !=" " :
            print(sentence[i+1])
        i+=1