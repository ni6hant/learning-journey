# Write your solution here

def even_numbers(inputList:list):
    new_list = []
    for item in inputList:
        if item%2==0:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    even_numbers([1,2,3,4,5])