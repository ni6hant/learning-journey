# Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 0:
        print("Bye now!")
        break
    if function == 2:
        with open("diary.txt") as my_file:
            for line in my_file:
                print(line.strip())
    if function == 1:
        entry = input("Diary entry:")
        with open("diary.txt", "a") as my_file:
            my_file.write(f"{entry}\n")
        print("Diary saved")