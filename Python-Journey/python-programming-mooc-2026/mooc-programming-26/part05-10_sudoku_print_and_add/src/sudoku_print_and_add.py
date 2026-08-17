# Write your solution here
def print_row(row:list):
    count = 0
    for item in row:
        #if 0 replace with -
        if item==0:
            print("_",end="")
        else:
            print(item,end="")

        #add two space after 3,6 and for rest add one space after except from the last one
        count+=1
        if count==9:
            print("")
        elif count%3==0:
            print("  ",end="")
        else: #count%3!=0
            print(" ",end="")

def print_sudoku(sudoku:list):
    count=0
    #loop through each row
    for row in sudoku:
        print_row(row) #print each row
        count+=1
        if count%3==0 and count%9!=0: #after 3,6 row add a blank line
            print()
    return

def add_number(sudoku:list, row_no:int, column_no:int, number:int):
    sudoku[row_no][column_no]=number
    return sudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)