# Write your solution here
year = int(input("Year: "))

tempYear = year+1
while True: 
    if tempYear%100 == 0:
        if tempYear%400 == 0:
            nextLeapYear = tempYear
            break
        else:
            nextLeapYear = tempYear + 4
            break
    elif tempYear%4 == 0:
        nextLeapYear = tempYear
        break
    else:
        tempYear = tempYear + 1

print(f"The next leap year after {year} is {nextLeapYear}")
