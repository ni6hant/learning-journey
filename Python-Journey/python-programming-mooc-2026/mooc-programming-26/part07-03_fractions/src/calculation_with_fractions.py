# Write your solution here
from fractions import Fraction

def fractionate(denom:int):
    fractionate_list = []
    for i in range(0,denom):
        fractionate_list.append(Fraction(1,denom))
    return fractionate_list

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)
    print()
    print(fractionate(5))