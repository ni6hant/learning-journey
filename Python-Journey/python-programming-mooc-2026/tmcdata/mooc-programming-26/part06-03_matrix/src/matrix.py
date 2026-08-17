# write your solution here

def matrix_sum():
    
    total_sum=0
    with open("matrix.txt") as new_file:
        for line in new_file:
            flag = True

            parts=[]
            line = line.replace("\n", "")
            parts = line.split(",")
            sum=0
            sum_list=[]
            for item in parts:
                sum+=int(item)
            sum_list.append(sum)
            
            for item in sum_list:
                total_sum+=item
    return total_sum

def matrix_max():
    largest_list=[]
    with open("matrix.txt") as new_file:
        for line in new_file:
            flag = True

            parts=[]
            line = line.replace("\n", "")
            parts = line.split(",")

            for item in parts:
                if flag:
                    largest=int(item)
                    flag=False
                else:
                    if largest<int(item):
                        largest=int(item)

            largest_list.append(largest)
    return max(largest_list)

def row_sums():
    #sum of each row in the matrix
    sum_list=[]
    
    with open("matrix.txt") as new_file:
        for line in new_file:
            flag = True

            parts=[]
            line = line.replace("\n", "")
            parts = line.split(",")
            sum=0
            for item in parts:
                sum+=int(item)
            sum_list.append(sum)
    return sum_list

if __name__ == "__main__":
    matrix_max()
    matrix_sum()