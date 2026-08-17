# Write your solution here

import string

def print_row(layer_from_middle:int, max_layer:int):
    letters = string.ascii_uppercase
    max_char = max_layer - layer_from_middle #Maximum number of character in that particular row
    length_of_string = 2*max_layer - 1
    outer_most_character = letters[max_layer-1]
    output = [outer_most_character]*length_of_string

    max_range = max_layer - 2

    for i in range(0,max_char-1):
        for j in range(-max_range,max_range+1):
            output[j+max_layer-1]=letters[max_layer-2-i]
        max_range-=1

    return output


layers = int(input("Layers: "))


for i in range(-(layers-1),(layers-1)+1):
    row = print_row(abs(i),layers)
    for item in row:
        print(item,end="")
    print()