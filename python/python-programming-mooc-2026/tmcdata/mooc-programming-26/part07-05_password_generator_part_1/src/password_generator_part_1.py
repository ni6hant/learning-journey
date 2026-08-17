# Write your solution here
from random import randint
import string

def generate_password(max_length):
    password = ""
    for i in range(0,max_length):
        password+=string.ascii_lowercase[randint(0,25)]
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))