# write your solution here
def largest():
    with open("numbers.txt") as new_file:

        flag = True

        for line in new_file:
            line = int(line.replace("\n",""))

            #store the first value then skip all else
            if flag:
                largest_number = line
            flag = False

            if largest_number<line:
                largest_number = line
    return largest_number

if __name__ == "__main__":
    largest()