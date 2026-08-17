# Write your solution here
def distinct_numbers(inputListOfIntegers:list):
    sortedListOfIntegers = sorted(inputListOfIntegers)
    distinct_numbers_calculated = []
    for item in sortedListOfIntegers:
        if item not in distinct_numbers_calculated:
            distinct_numbers_calculated.append(item)
    return distinct_numbers_calculated

if __name__ == "__main__":
    distinct_numbers([3,2,2,1,3,3,1])