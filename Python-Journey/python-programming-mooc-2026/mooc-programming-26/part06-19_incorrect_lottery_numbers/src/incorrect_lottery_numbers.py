# Write your solution here
def filter_incorrect():
    filtered_data = []
    with open("lottery_numbers.csv") as file:
        for line in file:
            flag=True
            parts=line.split(";")

            first = parts[0].split(" ")
            try: #The week number is incorrect:
                week = int(first[1])
            except:
                continue
            
            second = parts[1].split(",")
            numbers=[]
            for items in second:
                try: #One or more numbers are not correct:
                    numbers.append(int(items))
                except:
                    continue
            # Too few numbers:
            if len(numbers)!=7:
                continue
            for item in numbers: #The numbers are too small or large:
                if item<1 or item>39 or numbers.count(item)>1: #The same number appears twice:
                    flag=False
            if flag:
                filtered_data.append(line)

    with open("correct_numbers.csv","w") as new_file:
        for line in filtered_data:
            new_file.write(line)
    return 

if __name__ == "__main__":
    filter_incorrect()