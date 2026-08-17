# Write your solution here
def store_personal_data(person:tuple):
    with open("people.csv", "a") as my_file:
        my_file.write(f"{person[0]};{person[1]};{person[2]:0.1f}\n")
    

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))