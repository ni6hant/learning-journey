# Copy here code of line function from previous exercise and use it in your solution

def line(number,string):
    if string:
        print(string[0]*number)
    else:
        print("*"*number)

def triangle(size, character):
    # You should call function line here with proper parameters
    count = 0
    while count<size:
        line(count+1, character)
        count +=1

def rectangle(width, height, character):
    # You should call function line here with proper parameters
    count = 0
    while count<height:
        line(width, character)
        count +=1

def shape(traingleSize, triangleCharacter, squareSize, squareCharacter):
    triangle(traingleSize,triangleCharacter)
    rectangle(traingleSize,squareSize, squareCharacter)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    # shape(traingleSize, triangleCharacter, squareSize, squareCharacter)
    shape(5, "X", 3, "*")