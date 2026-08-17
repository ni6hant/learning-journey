# Write your solution here
def factorials(n:int):
    my_dictionary = {}
    my_dictionary[1] = 1  
    if n<2:
        return my_dictionary
    for i in range(2,n+1):
        my_dictionary[i] = i*my_dictionary[i-1]
    return my_dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])