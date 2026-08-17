# Write your solution here

def remove_smallest(numbers:list):
    smallest = numbers[0]
    for item in numbers:
        if smallest>item:
            smallest = item
    numbers.remove(smallest)

if __name__ == "__main__":
    numbers = [1, 2, 3, 5, 6]
    remove_smallest(numbers)
    print(numbers)