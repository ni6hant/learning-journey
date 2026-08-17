# Write your solution here
def filter_solutions():
    correct_list=[]
    incorrect_list=[]
    with open("solutions.csv") as my_file:
        for line in my_file:
            parts = line.strip().split(";")
            if "+" in parts[1]:
                values = parts[1].split("+")
                correct = int(values[0]) + int(values[1])
            if "-" in parts[1]:
                values = parts[1].split("-")
                correct = int(values[0]) - int(values[1])
            if correct == int(parts[2]):
                correct_list.append(line)
            else:
                incorrect_list.append(line)

# Clear files before writing to them.
    with open("correct.csv", "w") as my_file:
        pass         
    with open("incorrect.csv", "w") as my_file:
        pass

    with open("correct.csv", "a") as my_file:
        for item in correct_list:
            my_file.write(item)

    with open("incorrect.csv", "a") as my_file:
        for item in incorrect_list:
            my_file.write(item)

if __name__ == "__main__":
    filter_solutions()