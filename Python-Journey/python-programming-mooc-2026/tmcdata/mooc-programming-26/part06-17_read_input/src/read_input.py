# Write your solution here
def read_input(test:int,lower:int,upper:int):
    while True:
        try:
            test = input("Please type in a number: ")
            if lower<int(test)<upper:
                return int(test)
        except:
            pass
        print(f"You must type in an integer between {lower} and {upper}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)