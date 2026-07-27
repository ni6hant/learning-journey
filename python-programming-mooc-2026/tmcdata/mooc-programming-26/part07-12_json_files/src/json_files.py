# Write your solution here
import json

def read_file(filename:str):
    try:
        with open(filename) as new_file:
            data = json.loads(new_file.read())
    except:
        print("File could not be read")
    return data

def print_persons(filename:str):
    data = read_file(filename)
    for person in data:
        print(f"{person['name']} {person['age']} years ({", ".join(person['hobbies'])})")
    return data

if __name__ == "__main__":
    print_persons("file1.json")
    print("----------------------------------------------")
    print_persons("file2.json")
    print("----------------------------------------------")
    print_persons("file3.json")
    print("----------------------------------------------")
    print_persons("file4.json")
