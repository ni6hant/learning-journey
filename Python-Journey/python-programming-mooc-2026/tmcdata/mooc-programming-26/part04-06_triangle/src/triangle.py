# Copy here code of line function from previous exercise
def line(number,string):
    if string:
        print(string[0]*number)
    else:
        print("*"*number)

def triangle(size):
    # You should call function line here with proper parameters
    count = 0
    while count<size:
        line(count+1, "#")
        count +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
