# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    check=[]
    i=0
    j=0
    #elements start from 0,0 to 0+2,0+2 included or 0+3), 0+3)
    for i in range(row_no,row_no+3):
        # sudoku[i] now returns that row
        for j in range(column_no,column_no+3):
            #sukoku[i][j] now returns that element
            if sudoku[i][j] in check and sudoku[i][j]>0:
                return False
            else:
                check.append(sudoku[i][j])
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))