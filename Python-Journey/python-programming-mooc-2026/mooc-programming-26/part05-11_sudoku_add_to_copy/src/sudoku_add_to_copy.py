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


def copy_and_add(sudoku:list, row_no:int, column_no:int, number:int):
    copy_sudoku=[]
    for row in sudoku:
        copy_sudoku.append(row[:])
    copy_sudoku[row_no][column_no]=number
    return copy_sudoku

if __name__=="__main__":
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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
