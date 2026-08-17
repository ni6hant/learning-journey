# Programming exercise:
# Taking turns
# Points:
# 0

# /

# 1

# Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

# Sample output
# Please type in a number: 5
# 1
# 5
# 2
# 4
# 3

# Sample output
# Please type in a number: 6
# 1
# 6
# 2
# 5
# 3
# 4

number = int(input("Please type in a number: "))
i=1
j=number

if number>=1:
    # Loop 1: goes from 1 to and including number+1/2 both in even and in odd
    while i<=((number+1)/2):
        # Loop 2: starts from the number and then decreases by 1. 
        print(i)
        if j>(number/2) and j!=i:
            print(j)
            j-=1
            #if even stops at > number/2
            #if odd, stops at > number /2
        i+=1