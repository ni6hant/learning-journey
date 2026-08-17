while True:
    editori = str(input("Editor: "))
    if editori.lower() == "visual studio code":
        break
    if editori.lower() == "word" or editori.lower() == "notepad":
        print("awful")
    else:
        print("not good")
print("an excellent choice!")

