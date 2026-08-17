# Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:

# chessboard(3)
# print()
# chessboard(6)
# Sample output
# 101
# 010
# 101

# 101010
# 010101
# 101010
# 010101
# 101010
# 010101

# Write your solution here
def chessboard(length):
    i=1
    if length%2!=0:
        while i<=length:
            if i%2==0:
                print("01"*int(length/2)+"0")
            else:
                print("1"+"01"*int(length/2))
            i+=1
    else:
        while i<=length:
            if i%2==0:
                print("01"*int(length/2))
            else:
                print("10"*int(length/2))
            i+=1


# Testing the function
if __name__ == "__main__":
    chessboard(5)
