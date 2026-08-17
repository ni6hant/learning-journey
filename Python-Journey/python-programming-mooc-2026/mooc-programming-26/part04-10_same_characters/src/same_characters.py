# Write your solution here
def same_chars(string,i,j):
    if i>=len(string) or j>=len(string):
        return False
    return string[i]==string[j]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))