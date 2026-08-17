# Write your solution here
from math import sqrt

def hypotenuse(leg1:float,leg2:float):
    largest_side = sqrt(leg1*leg1 + leg2*leg2)
    return largest_side

if __name__ == "__main__":
    hypotenuse()