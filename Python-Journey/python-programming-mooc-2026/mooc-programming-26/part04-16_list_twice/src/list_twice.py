# Write your solution here
original = [2, 5, 1, 2, 4]
in_order = sorted(original)



list = []
count=0

while True:
    temp = int(input("New Item: "))    
    if temp == 0:
        print("Bye!")
        break
    else:
        list.append(temp)
        count+=1
        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")
