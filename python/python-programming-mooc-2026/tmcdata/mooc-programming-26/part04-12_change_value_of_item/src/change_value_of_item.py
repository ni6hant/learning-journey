# Write your solution here

inputList = [1,2,3,4,5]
index = 0

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    newValue = int(input("New value: "))
    inputList[index] = newValue
    print(inputList)
