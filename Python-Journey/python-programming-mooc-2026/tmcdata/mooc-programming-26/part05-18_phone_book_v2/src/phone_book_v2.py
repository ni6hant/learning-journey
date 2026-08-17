def search(persons):
    name = input("name: ")
    if name in persons:
        for numbers in persons[name]:
            print(numbers)
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    if name not in persons:
        persons[name] = []
    number = input("number: ")
    persons[name].append(number)
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")

main()