# Write your solution here

def create_tuple(x: int, y: int, z: int):
    integers = [x,y,z]
    greatest = max(integers)
    smallest = min(integers)
    total = sum(integers)
    return (smallest,greatest,total)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))