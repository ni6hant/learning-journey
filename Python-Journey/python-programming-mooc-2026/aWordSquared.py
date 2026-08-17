# Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

# squared("ab", 3)
# print()
# squared("aybabtu", 5)
# Sample output
# aba
# bab
# aba

# aybab
# tuayb
# abtua
# ybabt
# uayba

# Or,
# aybabtu aybabtu aybabtu aybabtu aybabtu
# aybab
#      tu ayb
# 	         abtu a
# 		           ybabt
#                       u ayba             
# Total no. of characters to print = count*count
# repeatedString should have atleast count*count characters and should be repeated count*count/len(string) times          

# def squared(string,count):
#     repeatedString = string*(int(1+(count*count)/len(string)))
#     i = 0
#     j=0
#     while i<count:
#         print(repeatedString[j:j+count])
#         i+=1
#         j+=count

def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)
# Write your solution here        

# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)