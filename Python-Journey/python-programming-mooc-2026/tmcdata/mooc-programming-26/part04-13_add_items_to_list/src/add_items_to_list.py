# Write your solution here

totalItems = int(input("How many items: "))
i = 0
list =[]

while i<totalItems:
    item = int(input(f"Item {i+1}: ")) 
    list.append(item)
    i+=1

print(list)