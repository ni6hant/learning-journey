# Write your solution here
def new_person(name:str, age:int):
    if name=="":
        raise ValueError("Name is empty")
    parts = name.split(" ")
    if len(parts) < 2:
        raise ValueError("Name contains less than two words")
    if len(name)>40:
        raise ValueError("Name is longer than 40 characters")
    if int(age)<0:
        raise ValueError("Age is a negative number")
    if int(age)>150:
        raise ValueError("Age is greater than 150")
    value = name, int(age)
    return value

    

if __name__ == "__main__":
    test_cases = [('Andrew', 32), ("",11), ("Mary", 33), ("Sirkka-Liisa Virtanen-Aftenbladet-Totterstrom-Lahtiska-Vanamo-Kullervoinen", 97)]
    for test_case in test_cases:
        new_person(test_case[0],test_case[1])