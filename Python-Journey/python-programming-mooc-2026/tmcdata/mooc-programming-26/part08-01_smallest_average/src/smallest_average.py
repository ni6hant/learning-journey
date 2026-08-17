# Write your solution here
def average(person:dict):
    average = (person["result1"]+person["result2"]+person["result3"])/3
    return average

def smallest_average(person1: dict, person2: dict, person3: dict):
    average_dict = {}
    average_dict = {
        average(person1) : person1,
        average(person2) : person2,
        average(person3) : person3
    }
    return average_dict[min(average_dict.keys())]

if __name__ == "__main__":
    person1 = {"name": "Anna", "result1": 9, "result2": 9, "result3": 9}
    person2 = {"name": "Anna", "result1": 7, "result2": 7, "result3": 7}
    person3 = {"name": "Anna", "result1": 8, "result2": 8, "result3": 8}

    print(smallest_average(person1, person2, person3))
