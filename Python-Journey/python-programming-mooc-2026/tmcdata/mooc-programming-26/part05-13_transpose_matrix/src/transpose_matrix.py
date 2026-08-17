# Write your solution here
def transpose(matrix:list):
    copy_matrix = []
    length_of_matrix = len(matrix[0])
    for row in matrix:
        copy_matrix.append(row[:])

    for i in range(0,length_of_matrix):
        for j in range(0,length_of_matrix):
            matrix[i][j] = copy_matrix[j][i]

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    transpose(matrix)
    print("After transposing")
    print(matrix)