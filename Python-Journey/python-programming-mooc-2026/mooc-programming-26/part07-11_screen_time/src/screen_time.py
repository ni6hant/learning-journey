# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")

try:
    with open(filename) as my_file:
        pass
except:
    print("Can't open file")

starting_date_str = input("Starting date: ")
try:
    starting_date = datetime.strptime(starting_date_str, "%d.%m.%Y")
except:
    print("Incorrect date format. It should be in the format dd.mm.yyyy")

try:
    days = int(input("How many days: "))
except:
    print("Days shoulbe be numeral only")

print("Please type in screen time in minutes on each day (TV computer mobile):")

screenTime = []
total_minutes = 0

for i in range(0,days):
    current_date = (starting_date+timedelta(days=i)).strftime("%d.%m.%Y")
    times = input(f"Screen time {current_date}: ")
    parts = []
    try:
        for mins in times.split(" "):
            mins_number = int(mins)
            parts.append(mins_number)
        total_minutes += sum(parts)
    except:
        print("Time should in the format: 180 0 0 i.e. three values for minutes separated by a blank space")
    screenTime.append([current_date,parts])

try:
    with open(filename,"w") as my_file:
        my_file.write(f"Time period: {screenTime[0][0]}-{screenTime[-1][0]}\n")
        my_file.write(f"Total minutes: {total_minutes}\n")
        my_file.write(f"Average minutes: {total_minutes/days:0.1f}\n")
        for st in screenTime:
            my_file.write(f"{st[0]}: {st[1][0]}/{st[1][1]}/{st[1][2]}\n")
except:
    print("There was an error when reding the file.")

print("Data stored in file late_june.txt")