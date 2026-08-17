# Write your solution here
def formatted(inputList:list):
    new_list = []
    for item in inputList:
        new_list.append(f"{item:.2f}")
    return new_list

if __name__ == "__main__":
    formatted([1.234, 0.3333, 0.11111, 3.446])