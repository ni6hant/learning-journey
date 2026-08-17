# Write your solution here

def list_sum(inputList1:list,inputList2:list):
    sum_of_lists = []
    for i in range(len(inputList1)):
        sum_of_lists.append(inputList1[i] + inputList2[i])
    return sum_of_lists

if __name__ == "__main__":
    list_sum([1, 2, 3],[7, 8, 9])