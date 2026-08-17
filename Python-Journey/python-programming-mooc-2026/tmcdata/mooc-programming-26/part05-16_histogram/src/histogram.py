# Write your solution here

def histogram(my_str:str):
    hist_dict = {}
    for char in my_str:
        if char not in hist_dict:
            hist_dict[char]=0
        hist_dict[char] += 1
    for key,value in hist_dict.items():
        print(key,end=" ")
        print(value*"*")

if __name__ == "__main__":
    histogram("abba")