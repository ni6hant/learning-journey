list = []
count=0

while True:
    temp = str(input("Word: "))    
    if temp in list:
        break
    else:
        list.append(temp)
        count+=1
print(f"You typed in {count} different words")

