# Write your solution here

def count_matching_elements(matrix:list,matching_number:int):
    count = 0
    for row in matrix:
        for item in row:
            if item==matching_number:
                count+=1
    return count

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))