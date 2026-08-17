# Write your solution here

def sum_of_positives(my_list:list):
    sum=0
    for item in my_list:
        if item>0:
            sum+=item
    return sum

if __name__ == "__main__":
    sum_of_positives([1,-2,3,-4,5])