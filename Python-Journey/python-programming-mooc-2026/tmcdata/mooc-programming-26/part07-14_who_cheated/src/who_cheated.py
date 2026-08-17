# Write your solution here
import csv
from datetime import timedelta, datetime


def start_times_process(filename):
    start_times_dict = {}
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            start_times_dict[line[0]] = datetime.strptime("1:"+line[1], "%d:%H:%M") #Default to day 1
        return start_times_dict


def submission_process(filename):
    submission_list = []
    with open(filename) as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            # name;task;points;hh:mm
            submission_list.append([line[0],int(line[1]),int(line[2]),datetime.strptime("1:"+line[3], "%d:%H:%M")])
    return sorted(submission_list)


def cheaters():
    cheaters_list = []
    start_data = start_times_process("start_times.csv")
    submission_data = submission_process("submissions.csv")
    for item in submission_data:
        if item[3]-start_data[item[0]]>timedelta(hours=3) and item[0] not in cheaters_list:
            cheaters_list.append(item[0])
    return cheaters_list

if __name__ == "__main__":
    print(cheaters())